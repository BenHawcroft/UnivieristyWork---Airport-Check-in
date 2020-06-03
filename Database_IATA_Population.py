import sqlite3


CREATE TABLE airports (
    `name` VARCHAR(56) CHARACTER SET utf8,
    `code` VARCHAR(3) CHARACTER SET utf8,
    `stateCode` VARCHAR(2) CHARACTER SET utf8,
    `countryCode` VARCHAR(2) CHARACTER SET utf8,
    `countryName` VARCHAR(32) CHARACTER SET utf8
);
INSERT INTO airports VALUES ('Anaa','AAA',NULL,'PF','French Polynesia');
INSERT INTO airports VALUES ('Annaba Les Salines','AAE',NULL,'DZ','Algeria');
INSERT INTO airports VALUES ('Aalborg','AAL',NULL,'DK','Denmark');