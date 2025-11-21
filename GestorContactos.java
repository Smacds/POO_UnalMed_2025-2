import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.File;
import java.io.IOException;
import java.io.RandomAccessFile;

public class GestorContactos extends JFrame implements ActionListener {

    private final String RUTA_ARCHIVO = "c:/Users/seyka/OneDrive/Documentos/Universidad Nacional/10. Decimo semestre/POO/Codigos/Taller5.txt";
    private final String SEPARADOR = "!";

    // Componentes de la Interfaz
    private JTextField txtNombre, txtNumero;
    private JButton btnAgregar, btnLeer, btnActualizar, btnEliminar, btnLimpiar;
    private JTextArea areaSalida;

    public GestorContactos() {
        super("Gestión de Contactos - CRUD");
        setSize(600, 500);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(new BorderLayout(10, 10));
        setLocationRelativeTo(null);

        JPanel panelEntrada = new JPanel(new GridLayout(3, 2, 5, 5));
        panelEntrada.setBorder(BorderFactory.createEmptyBorder(10, 10, 0, 10));

        panelEntrada.add(new JLabel("Nombre:"));
        txtNombre = new JTextField();
        panelEntrada.add(txtNombre);

        panelEntrada.add(new JLabel("Número:"));
        txtNumero = new JTextField();
        panelEntrada.add(txtNumero);

        panelEntrada.add(new JLabel(""));

        panelEntrada.add(new JLabel(""));

        add(panelEntrada, BorderLayout.NORTH);

        // --- PANEL CENTRAL (Botones) ---
        JPanel panelBotones = new JPanel(new FlowLayout());

        btnAgregar = new JButton("Agregar");
        btnLeer = new JButton("Leer Todos");
        btnActualizar = new JButton("Actualizar");
        btnEliminar = new JButton("Eliminar");
        btnLimpiar = new JButton("Limpiar Campos");

        // Asignar listeners
        btnAgregar.addActionListener(this);
        btnLeer.addActionListener(this);
        btnActualizar.addActionListener(this);
        btnEliminar.addActionListener(this);
        btnLimpiar.addActionListener(this);

        panelBotones.add(btnAgregar);
        panelBotones.add(btnLeer);
        panelBotones.add(btnActualizar);
        panelBotones.add(btnEliminar);
        panelBotones.add(btnLimpiar);

        add(panelBotones, BorderLayout.CENTER);

        // --- PANEL INFERIOR (Salida) ---
        areaSalida = new JTextArea(15, 40);
        areaSalida.setEditable(false);
        JScrollPane scroll = new JScrollPane(areaSalida);
        scroll.setBorder(BorderFactory.createTitledBorder("Resultados / Consola"));

        add(scroll, BorderLayout.SOUTH);
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        if (e.getSource() == btnAgregar) {
            crearContacto();
        } else if (e.getSource() == btnLeer) {
            leerContactos();
        } else if (e.getSource() == btnActualizar) {
            actualizarContacto();
        } else if (e.getSource() == btnEliminar) {
            eliminarContacto();
        } else if (e.getSource() == btnLimpiar) {
            limpiarCampos();
        }
    }

    // OPERACIÓN 1: AGREGAR
    private void crearContacto() {
        String nuevoNombre = txtNombre.getText().trim();
        String nuevoNumeroStr = txtNumero.getText().trim();

        if (nuevoNombre.isEmpty() || nuevoNumeroStr.isEmpty()) {
            areaSalida.setText("Error: Debes ingresar nombre y número.");
            return;
        }

        try {
            long nuevoNumero = Long.parseLong(nuevoNumeroStr);
            File file = new File(RUTA_ARCHIVO);

            // Asegurar que el directorio exista
            if (file.getParentFile() != null) {
                file.getParentFile().mkdirs();
            }
            if (!file.exists()) {
                file.createNewFile();
            }

            try (RandomAccessFile raf = new RandomAccessFile(file, "rw")) {
                boolean encontrado = false;

                // Buscar duplicados
                raf.seek(0);
                while (raf.getFilePointer() < raf.length()) {
                    String linea = raf.readLine();
                    if (linea == null)
                        continue;

                    String[] partes = linea.split(SEPARADOR);
                    if (partes.length >= 2) {
                        String nombreExistente = partes[0];
                        long numeroExistente = Long.parseLong(partes[1]);

                        if (nombreExistente.equals(nuevoNombre) || numeroExistente == nuevoNumero) {
                            encontrado = true;
                            break;
                        }
                    }
                }

                if (!encontrado) {
                    String registro = nuevoNombre + SEPARADOR + nuevoNumero;
                    raf.seek(raf.length()); // Ir al final
                    raf.writeBytes(registro);
                    raf.writeBytes(System.lineSeparator());
                    areaSalida.setText("Amigo agregado: " + nuevoNombre);
                    limpiarCampos();
                } else {
                    areaSalida.setText("El nombre o número ya existe.");
                }
            }
        } catch (NumberFormatException nfe) {
            areaSalida.setText("Error: El número no es válido.");
        } catch (IOException io) {
            areaSalida.setText("Error IO: " + io.getMessage());
        }
    }

    // OPERACIÓN 2: LEER
    private void leerContactos() {
        areaSalida.setText(""); // Limpiar pantalla
        File file = new File(RUTA_ARCHIVO);

        if (!file.exists()) {
            areaSalida.setText("El archivo no existe aún.");
            return;
        }

        try (RandomAccessFile raf = new RandomAccessFile(file, "rw")) {
            areaSalida.append("--- LISTA DE CONTACTOS ---\n");
            raf.seek(0);
            while (raf.getFilePointer() < raf.length()) {
                String linea = raf.readLine();
                if (linea == null)
                    continue;

                String[] partes = linea.split(SEPARADOR);
                if (partes.length >= 2) {
                    areaSalida.append("Nombre: " + partes[0] + " | Número: " + partes[1] + "\n");
                }
            }
        } catch (IOException io) {
            areaSalida.setText("Error al leer: " + io.getMessage());
        }
    }

    // OPERACIÓN 3: ACTUALIZAR

    private void actualizarContacto() {
        String nombreBuscado = txtNombre.getText().trim();
        String nuevoNumeroStr = txtNumero.getText().trim();

        if (nombreBuscado.isEmpty() || nuevoNumeroStr.isEmpty()) {
            areaSalida.setText("Para actualizar, escribe el Nombre exacto y el Nuevo Número.");
            return;
        }

        try {
            long nuevoNumero = Long.parseLong(nuevoNumeroStr);
            gestionarArchivoTemporal(nombreBuscado, nuevoNumero, "UPDATE");
        } catch (NumberFormatException e) {
            areaSalida.setText("El nuevo número no es válido.");
        }
    }

    // OPERACIÓN 4: ELIMINAR

    private void eliminarContacto() {
        String nombreBuscado = txtNombre.getText().trim();

        if (nombreBuscado.isEmpty()) {
            areaSalida.setText("Para eliminar, escribe el Nombre exacto.");
            return;
        }

        gestionarArchivoTemporal(nombreBuscado, 0, "DELETE");
    }

    private void gestionarArchivoTemporal(String nombreObjetivo, long numeroActualizar, String modo) {
        File archivoOriginal = new File(RUTA_ARCHIVO);
        File archivoTemporal = new File("temp.txt"); // Se crea en la carpeta del proyecto

        if (!archivoOriginal.exists()) {
            areaSalida.setText("El archivo de contactos no existe.");
            return;
        }

        try (RandomAccessFile raf = new RandomAccessFile(archivoOriginal, "rw");
                RandomAccessFile tmpRaf = new RandomAccessFile(archivoTemporal, "rw")) {

            raf.seek(0);
            tmpRaf.setLength(0); // Asegurar temp vacío
            boolean encontrado = false;

            while (raf.getFilePointer() < raf.length()) {
                String linea = raf.readLine();
                if (linea == null)
                    continue;

                String[] partes = linea.split(SEPARADOR);

                if (partes.length < 2)
                    continue;

                String nombreActual = partes[0];

                if (nombreActual.equals(nombreObjetivo)) {
                    encontrado = true;
                    if (modo.equals("UPDATE")) {

                        String nuevaLinea = nombreActual + SEPARADOR + numeroActualizar;
                        tmpRaf.writeBytes(nuevaLinea);
                        tmpRaf.writeBytes(System.lineSeparator());
                    }

                } else {

                    tmpRaf.writeBytes(linea);
                    tmpRaf.writeBytes(System.lineSeparator());
                }
            }

            if (encontrado) {

                raf.seek(0);
                tmpRaf.seek(0);
                while (tmpRaf.getFilePointer() < tmpRaf.length()) {
                    raf.writeBytes(tmpRaf.readLine());
                    raf.writeBytes(System.lineSeparator());
                }

                raf.setLength(tmpRaf.length());

                areaSalida.setText("Operación " + modo + " realizada con éxito para: " + nombreObjetivo);
                if (modo.equals("DELETE"))
                    limpiarCampos();
            } else {
                areaSalida.setText("No se encontró el nombre: " + nombreObjetivo);
            }

        } catch (IOException e) {
            areaSalida.setText("Error IO: " + e.getMessage());
        } finally {

            if (archivoTemporal.exists()) {
                archivoTemporal.delete();
            }
        }
    }

    // ---------------------------------------------------------
    // BOTÓN 5: LIMPIAR CAMPOS
    // ---------------------------------------------------------
    private void limpiarCampos() {
        txtNombre.setText("");
        txtNumero.setText("");
        txtNombre.requestFocus();
    }

    public static void main(String[] args) {

        SwingUtilities.invokeLater(() -> {
            new GestorContactos().setVisible(true);
        });
    }
}