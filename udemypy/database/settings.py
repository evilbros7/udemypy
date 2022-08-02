from os import getenv

DATABASE_URL = getenv("DATABASE_URL")
COURSE_LIFETIME = int(getenv("COURSE_LIFETIME"))

RECONNECTION_ATTEMPTS = 4
UPDATE_DATABASE_COMMANDS = ("DELETE", "INSERT INTO", "CREATE TABLE")
