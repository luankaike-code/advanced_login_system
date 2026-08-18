DROP TABLE IF EXISTS users;

CREATE TABLE users (
	user_id INT PRIMARY KEY AUTO_INCREMENT,
	name VARCHAR(255) NOT NULL,
	email VARCHAR(255) UNIQUE NOT NULL,
	password VARCHAR(255) NOT NULL,
	tel VARCHAR(11) UNIQUE,
	has_sudo_access BOOL DEFAULT FALSE
);

INSERT INTO users (name, email, password, tel, has_sudo_access) VALUES (
	"root",
	"root@root",
	"@Root123",
	"00000000",
	TRUE
);