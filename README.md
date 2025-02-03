# Authentication and Security Scripts

This project contains Python scripts for implementing various authentication and security features, including user registration, login validation, form validation, password validation, and access control. These scripts use decorators, functions, and basic authentication mechanisms to simulate a secure environment for a web application.

## Scripts Overview

### 1. `control_de_acceso.py`
This script defines a decorator function, `verificar_acceso_entorno`, that checks the execution environment (e.g., "production" or "development") to control access to certain functions. It ensures that actions are only performed in the appropriate environment.

### 2. `cuenta_bancaria.py`
This script handles security-related features for a banking system. It may include authentication or validation related to bank account operations, ensuring secure access to financial data.

### 3. `inicio_sesion.py`
Contains a system for validating user credentials and logging into a system. The script uses a decorator `verificar_inicio_sesion` to validate the provided username and password against a predefined user registry before allowing access to the user's personal information.

### 4. `validacion_formulario.py`
This script validates a registration form, ensuring that:
- The name has a minimum length of 3 characters.
- The email contains both `@` and `.` characters.
- The phone number consists of 9 digits.

### 5. `validar_contrasena.py`
This script checks whether a given password meets specific security criteria, such as:
- A minimum length.
- Inclusion of uppercase and lowercase letters, numbers, and special characters.
It also provides suggestions for generating a secure password if the entered password is invalid.

## How to Use

1. Clone or download the repository.
2. Open a terminal or command prompt.
3. Run each script individually or modify them as needed for your use case.

For example, to validate a password using `validar_contrasena.py`:

```bash
python validar_contrasena.py
