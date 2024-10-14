SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";

CREATE TABLE `dataled` (
  `id` int NOT NULL,
  `kondidisi` tinyint DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `dataled` (`id`, `kondidisi`) VALUES
(1, 1);

ALTER TABLE `dataled`
  ADD PRIMARY KEY (`id`);

ALTER TABLE `dataled`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
COMMIT;
