import registeruser,checkvalidtion

email="kalam@gmail.com"
password="kalam01711"
kala=checkvalidtion.is_correct_email_formot(email)
print(kala)

registeruser.registration("kalam@gamil.com","kalam01711")
k=registeruser.start_with_hash_password(email,"kalam01711")
print(k)
