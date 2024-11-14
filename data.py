
headers = {
    "Authorization": f"Bearer {'authToken'}",
    "Content-Type": "application/json",

}

user_body = {
    "firstName": "Max",
    "phone": "+10005553535",
    "address": "8042 Lancaster Ave.Hamburg, NY"
}

kit_body = {
       "name": "Mi conjunto",
       "card": {
           "id": 1,
           "name": "Para la situación"
       },
       "productsList": "null",
       "id": 7,
       "productsCount": 0
   }

kit_body1 = {"name": "a"}
kit_body2 = {"name": "a"* 511}
kit_body3 = {"name": 0}
kit_body4 = {"name": "a" * 512}
kit_body5 = {"name": "\"№%@\"," }
kit_body6 = {"name": "A Aaa"}
kit_body7 = {"name": "123"}
kit_body8 = {}
kit_body9 = {"name": 123}