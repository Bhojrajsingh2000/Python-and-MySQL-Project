-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 27, 2024 at 01:21 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `atm`
--

-- --------------------------------------------------------

--
-- Table structure for table `atmsql`
--

CREATE TABLE `atmsql` (
  `atmCardNo` varchar(20) NOT NULL,
  `name` varchar(30) NOT NULL,
  `dob` varchar(20) NOT NULL,
  `fatherName` varchar(30) NOT NULL,
  `address` varchar(30) NOT NULL,
  `mobile` varchar(30) NOT NULL,
  `adharNo` varchar(30) NOT NULL,
  `pin` varchar(5) NOT NULL,
  `totalAmount` int(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `atmsql`
--

INSERT INTO `atmsql` (`atmCardNo`, `name`, `dob`, `fatherName`, `address`, `mobile`, `adharNo`, `pin`, `totalAmount`) VALUES
('439194419613', 'Bhojraj Singh', '08/08/2003', 'Dasarath Chauhan', 'Jartauli', '9927038901', '445983519183', '4459', 4000),
('743799846290', 'Divakar Chauhan', '08/08/2004', 'Dasarath Chauhan', 'Jartauli', '9927038901', '4459835192', '1122', 1800);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `atmsql`
--
ALTER TABLE `atmsql`
  ADD PRIMARY KEY (`atmCardNo`),
  ADD UNIQUE KEY `adharNo` (`adharNo`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
