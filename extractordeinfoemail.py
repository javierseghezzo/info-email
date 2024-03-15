#take email addres from user - strip: elimina los espacios en blanco
email = input("Ingrese su dirección de correo electrónico: ").strip()

username = email[:email.index('@')]

domain = email[email.index('@')+1:]

result = f"Your username = {username}\nYour domain = {domain}"
print(result)

