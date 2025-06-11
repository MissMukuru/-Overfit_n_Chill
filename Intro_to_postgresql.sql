CREATE TABLE cars (
brand VARCHAR(255),
model VARChAR(255),
year INT
)

SELECT * FROM cars

INSERT INTO cars(brand, model, year)
VALUES ('Ford', 'Mustang', 1964)

SELECT * FROM cars

INSERT INTO cars(brand,model, year)
VALUES 
	('Volvo', 'p1800', 1968),
  	('BMW', 'M1', 1978),
  	('Toyota', 'Celica', 1975)

SELECT * FROM cars

---TO ADD A COLUMN TO AN EXISTING TABLE---
ALTER TABLE cars
ADD color VARCHAR(255)

---the update statement is used to modify the values in existing records in a table---
UPDATE cars
SET color = 'red'
WHERE brand = 'Volvo'

SELECT * FROM cars

UPDATE cars 
SET color = 'white', year = 1970
WHERE brand = 'Toyota'

SELECT * FROM cars

---The ALTER TABLE statement is used to add, delete, or modify columns in an existing table---
ALTER TABLE cars
ALTER COLUMN year TYPE VARCHAR(4)

ALTER TABLE cars
ALTER COLUMN color TYPE VARCHAR(30)

---DROP COLUMN---
ALTER TABLE cars
DROP COLUMN color






















