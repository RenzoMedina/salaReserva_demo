import app 

def testSalaDisponibilidad():
    reservas = [
        {"sala":"A", "hora":"10:00"},
        {"sala":"A", "hora":"11:00"}
    ]

    nueva = {"sala":"A", "hora":"12:00"}
    assert app.verificarDisponibilidad(reservas, nueva) == True

def testSalaNoDisponible():
    reservas = [
        {"sala":"A", "hora":"10:00"},
        {"sala":"A", "hora":"11:00"}
    ]

    nueva = {"sala":"A", "hora":"11:00"}
    assert app.verificarDisponibilidad(reservas, nueva) == False