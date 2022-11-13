

CREATE TABLE task (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(128),
    subtitle VARCHAR(256),
    body TEXT,
    active BOOLEAN DEFAULT 1
);

INSERT INTO task (
    title,
    subtitle,
    body
) VALUES (
    "Wash the dishes",
    "Go outside and wash the dishes",
    "Either do it yourself or take it to the sink."

);

INSERT INTO task (
    title,
    subtitle,
    body
) VALUES (
    "Cook dinner",
    "Prepare the food",
    "Eat out tonigth."
);
