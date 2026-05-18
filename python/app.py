# ==========================================
# ARCHIVO: app.py
# ==========================================

import sys
import seleccionar_usuario


# ==========================================
# CERRAR TODO EL SISTEMA
# ==========================================
def cerrar_sistema():

    sys.exit()


# ==========================================
# VENTANA PRINCIPAL
# ==========================================
ventana = seleccionar_usuario.ventana

# Evento al presionar X
ventana.protocol(
    "WM_DELETE_WINDOW",
    cerrar_sistema
)

# Ejecutar aplicación
ventana.mainloop()