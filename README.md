# simple-encrypt

Basic scripts for encrypting and decrypting text using a password.

Don't rely on these, as they're likely not the most secure systems you can find, but they're fine for my simple use case. The goal was to implement a reasonably secure system with no outside dependencies and minimal complexity.

## Usage

```bash
$ echo "text to encrypt" | ./encrypt.py
Password: dummypass
gAAAAABdrOy2C8zJuA2mh0KcwhvkcLJ95EXYRFAgchCYi7deucQrtKfkdV6_p8Ddm9fTp-mvGU0AfSUKUt7Js3RzFQ3OsOe3sxU4PlaJ-iAp_H8j03--GOg=
```

```bash
$ echo "gAAAAABdrOy2C8zJuA2mh0KcwhvkcLJ95EXYRFAgchCYi7deucQrtKfkdV6_p8Ddm9fTp-mvGU0AfSUKUt7Js3RzFQ3OsOe3sxU4PlaJ-iAp_H8j03--GOg=" | ./decrypt.py
Password: dummypass
text to encrypt
```
