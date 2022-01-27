Jorge es un cliente nuestro de muchos años, nos ha pedido desarrollar una aplicación personal
para sus ahorros.
Él posee dos cuentas bancarias en bancos diferentes: Interbank dispone de una cuenta en
dólares y Scotiabank en soles.
Cuando el recibe algún pago en efectivo, lo deposita en su cuenta en soles. Sabiendo que
todos los pagos lo realizan en efectivo.

REQUERIMIENTOS:
Los depósitos al banco Scotiabank sólo lo realiza con billetes de 100 y 50 soles. 
Los depósitos al banco Interbank sólo lo realiza en miles de dólares. 
Cuando acumula en su cuenta en soles una cantidad que supera el equivalente a 1000 dólares realiza depósitos en su cuenta en dólares. 
Al final del día se debe mostrar un reporte de estado de cuenta, mostrando también el monto  en efectivo.
<!-- 
 1. la cuenta de scotiabank no debe superar los 1000 dolares
       (1000 soles * tipoCambio > 1000 dolares , false)
  Si el monto de la cuenta en scotiabank es nulo debe devolver false
  Si el monto es de  tipo string a un numero devolver false
  Si el monto es de  tipo undefined a un numero devolver false
 2. los depositos a scotiabank deben de ser multiplos de 50
#       (167, false)
#       (150, true)
# 3. Los depósitos al banco Interbank deben de ser multiplos de 1000
#       (1200, false)
#       (3000, true)
# 4. Dia sin operaciones
#       Estado Inicial:
#           Interbank: 100
#           Scotiabank: 100
#           Efectivo: 100
#       Estado final:
#           Interbank: 100
#           Scotiabank: 100
#           Efectivo: 100
#       No habrian operaciones.

# 5. Dia con retiro
#       Estado Inicial:
#           Interbank: 100
#           Scotiabank: 100
#           Efectivo: 100
#       Estado final:
#           Interbank: 100
#           Scotiabank: 50
#           Efectivo: 150
#       operacion valida 
-->