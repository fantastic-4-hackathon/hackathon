from extensions import db, bcrypt, jwt
password_hash = bcrypt.generate_password_hash("password").decode('utf-8')
print(password_hash)


print(bcrypt.check_password_hash('$2b$12$CgdezPrb8m9VftKyib1SdO./5D9E47ClpB3kuUElbPlCVgdqNvqp.','password'))