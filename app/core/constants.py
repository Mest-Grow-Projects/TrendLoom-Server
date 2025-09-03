messages = {
    "db_connection": "Database connection initialized...",
    "shutdown": "Application shutting down...",
    "app_title": "TrendLoom ecommerce API",
    "app_description": "A REST API to manage products",
    "app_version": "1.0.0",
    "welcome": "Welcome to the TrendLoom Ecommerce API"
}

error_messages = {
    "database_url": "DATABASE_URL environment variable is not set"
}

status_messages = {
    "not_found": "User not found",
    "conflict": "User with this email already exists",
    "credentials_error": "Could not validate credentials"
}

origins = [
    "http://localhost:4200",
    "http://localhost:8080",
]

validations = {
    "name": "Name must contain only letters and single spaces between words, no numbers or special characters allowed",
    "password": "Password must contain at least one uppercase letter, one lowercase letter, one number, and one special character",
    "code": "Verification OTP code must be a 6-digit number",
    "password_mismatch": "passwords don't match",
}

patterns_regex = {
    "name": "^(?! )[A-Za-z]+(?: [A-Za-z]+)*(?<! )$",
    "password": "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()\-_=+{};:,<.>])[A-Za-z\d!@#$%^&*()\-_=+{};:,<.>]{8,50}$",
    "code": "^\d{6}$",
}