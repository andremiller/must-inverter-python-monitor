import minimalmodbus

SERPORT = '/dev/ttyUSB0'
SERTIMEOUT = 0.5
SERBAUD = 19200

# Registers to retrieve data for
register_map = {
    25201 : ["Work state", 1, "map", {
        0 : "PowerOn",
        1 : "SelfTest",
        2 : "OffGrid",
        3 : "Grid-Tie",
        4 : "Bypass",
        5 : "Stop",
        6 : "Grid Charging"}],
    25205 : ["Battery voltage", 0.1, "V"],
    25206 : ["Inverter voltage", 0.1, "V"],
    25207 : ["Grid voltage", 0.1, "V"],
    25208 : ["BUS voltage", 0.1, "V"],
    25209 : ["Control current", 0.1, "A"],
    25210 : ["Inverter current", 0.1, "A"],
    25211 : ["Grid current", 0.1, "A"],
    25212 : ["Load current", 0.1, "A"],
    25213 : ["Inverter power(P)", 1, "W"],
    25214 : ["Grid power(P)", 1, "W"],
    25215 : ["Load power(P)", 1, "W"],
    25216 : ["Load percent", 1, "%"],
    25217 : ["Inverter complex power(S)", 1, "VA"],
    25218 : ["Grid complex power(S)", 1, "VA"],
    25219 : ["Load complex power(S)", 1, "VA"],
    25221 : ["Inverter reactive power(Q)", 1, "var"],
    25222 : ["Grid reactive power(Q)", 1, "var"],
    25223 : ["Load reactive power(Q)", 1, "var"],
    25225 : ["Inverter frequency", 0.01, "Hz"],
    25226 : ["Grid frequency", 0.01, "Hz"],
    25233 : ["AC radiator temperature", 1, "C"],
    25234 : ["Transformer temperature", 1, "C"],
    25235 : ["DC radiator temperature", 1, "C"],
    25273 : ["Battery power", 1, "W"],
    25274 : ["Battery current", 1, "A"],
}

def read_register_values(i, startreg, count):
    register_id = startreg
    results = i.read_registers(startreg, count)
    for r in results:
        if register_id in register_map:
            r_name = register_map[register_id][0] # Name
            if register_map[register_id][2] == "map": # Mapped value
                r_value = register_map[register_id][3][r]
            else: # Unit value
                r_value = str(r*register_map[register_id][1])+register_map[register_id][2]
            print(str(r_name) + " = " + r_value)
        register_id += 1

i = minimalmodbus.Instrument(SERPORT, 4)
i.serial.timeout=SERTIMEOUT
i.serial.baudrate = SERBAUD
read_register_values(i, 25201, 75)

