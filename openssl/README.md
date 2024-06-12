# OpenSSL

Files may be PEM (base64-encoded) and DER (binary) format
- PEM may include `.pem`, `.cert`, `.crt`, `.cer`, and `.key` extensions
- DER may include `.der` or `.cer`; check whether the `.cer` is binary or PEM by using `file` or opening in an editor

`keytool` is part of Oracle's JDKs, not OpenSSL

## Table of Headers

[OpenSSL pem.h](https://github.com/openssl/openssl/blob/master/include/openssl/pem.h)

| File Type | Encrypted | Begin Headers | Notes |
| -- | -- | -- | -- |
| PKCS1 | no | BEGIN RSA PRIVATE KEY | "traditional" format |
| PKCS7 | no | BEGIN PKCS7 ||
| PKCS8 | no | BEGIN PRIVATE KEY ||
| PKCS8 | yes | BEGIN ENCRYPTED PRIVATE KEY ||
| PKCS12 (binary) | yes | BEGIN CERTIFICATE and BEGIN PRIVATE KEY | private keys are displayed unencrypted when the P12 is opened |
| X.509 | no | BEGIN CERTIFICATE ||

## Viewing Files

You may need to convert file formats and pipe through standard output/input instead of `-in`

X.509 - View and/or Verify Certificates

	openssl x509 -text -noout -in cert.pem
	openssl verify -CAfile ca.crt cert.pem
	# may need -inform pem or -inform der

PEM Keys

	openssl rsa -text -noout -in key.pem

Certificate Signing Requests (CSRs)

	openssl req -text -noout -verify -in some.csr

PKCS7/P7B

	openssl pkcs7 -in ca-chain.p7b -print_certs
	openssl pkcs7 -in ca-chain.p7b -print_certs | openssl x509 -text -noout

PKCS12/PFX

	openssl pkcs12 -nodes -in some.p12

PKCS12 - View Cert Only

	openssl pkcs12 -nodes -in some.p12 | openssl x509 -text -noout
	openssl pkcs12 -nodes -in some.p12 | openssl x509 | openssl verify -CAfile ca.pem

PKCS12 - View Key Only

	openssl pkcs12 -nodes -in some.p12 | openssl rsa -text -noout

Java Keystores

	keytool -list -keystore somekeystore.jks
	keytool -list -keystore somekeystore.jks -v
	keytool -list -keystore somekeystore.jks -alias <alias> -v

Common OpenSSL Password Options

	-passin pass:your-password
	-passout pass:your-password

## Creating Container Files

PKCS7/P7B - CRL, CA Chains, and/or Certificates (no keys)

	openssl crl2pkcs7 -nocrl -certfile certs/ca-int.cert.pem -certfile certs/ca.cert.pem -out ca-chain.p7b

PKCS12/PFX - Contains Certificate(s) and Private Key

	openssl pkcs12 -export -inkey key.pem -in cert.pem -certfile ca-chain.cert.pem -name <alias> -out new.p12
	# -certfile adds "extra certificates"; -CAfile adds PEM-format file of CAs

JKS - Import CA and/or PEM Certificates

	keytool -keystore NewOrExistingKeystore.jks -alias CAIntermediate -import -file ca-int.cert.pem
	keytool -keystore NewOrExistingKeystore.jks -alias CARoot -import -file ca.cert.pem
	# to specify passwords and avoid prompts, add: -storepass <keystore-password> -noprompt

JKS - Import PKCS12 (contains both cert and key)

	keytool -importkeystore -srckeystore some.p12 -srcstoretype pkcs12 -destkeystore NewOrExistingKeystore.jks
	# to specify passwords and avoid prompts, add: -srcstorepass <src store password> -storepass <working store password> -keypass <private key password> -noprompt

## Adding and Removing Passwords

PKCS8 - Add a Password (creates a new AES256-encrypted P8 file); accepts multiple input types, not just other P8 files

	openssl pkcs8 -topk8 -in plaintext.key -out encrypted.key

PKCS8 - Remove a Password (creates a new file)

	openssl rsa -in encrypted.key -out plaintext.key
	openssl pkcs8 -in encrypted.key -out plaintext.key
