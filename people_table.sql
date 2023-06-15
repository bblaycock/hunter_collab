use test;
CREATE TABLE `people_table` (
  `First_name` varchar(64) NOT NULL,
  `Last_name` varchar(45) DEFAULT NULL,
  `Age` int DEFAULT NULL,
  `Favorite_color` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`First_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
