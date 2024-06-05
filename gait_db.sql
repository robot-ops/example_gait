-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 05, 2024 at 06:29 AM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 8.1.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `gait_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `manage_users`
--

CREATE TABLE `manage_users` (
  `user_id` int(10) NOT NULL,
  `username` varchar(100) NOT NULL,
  `user_email` varchar(100) NOT NULL,
  `user_pass` varchar(100) NOT NULL,
  `full_name` varchar(100) NOT NULL,
  `creationDate` timestamp NOT NULL DEFAULT current_timestamp(),
  `updationDate` timestamp NULL DEFAULT NULL ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `tbldoctor`
--

CREATE TABLE `tbldoctor` (
  `doctorId` int(10) NOT NULL,
  `doctorName` varchar(100) NOT NULL,
  `doctorEmail` varchar(100) NOT NULL,
  `doctorUsername` varchar(100) DEFAULT NULL,
  `doctorPassword` varchar(100) NOT NULL,
  `creationDate` timestamp NOT NULL DEFAULT current_timestamp(),
  `updationDate` timestamp NULL DEFAULT NULL ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tbldoctor`
--

INSERT INTO `tbldoctor` (`doctorId`, `doctorName`, `doctorEmail`, `doctorUsername`, `doctorPassword`, `creationDate`, `updationDate`) VALUES
(1, 'admin', 'admin@gmail.com', NULL, 'admin', '2024-06-05 03:51:09', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `tblpatient`
--

CREATE TABLE `tblpatient` (
  `patientId` int(10) NOT NULL,
  `doctorId` int(10) NOT NULL,
  `patientName` varchar(100) NOT NULL,
  `patientAge` int(10) NOT NULL,
  `patientGender` varchar(100) NOT NULL,
  `patientWeight` double NOT NULL,
  `patientHeight` double NOT NULL,
  `patientMedic` varchar(100) NOT NULL,
  `emg1` varchar(100) NOT NULL,
  `emg2` varchar(100) NOT NULL,
  `emg3` varchar(100) NOT NULL,
  `emg4` varchar(100) NOT NULL,
  `leftHip` varchar(100) NOT NULL,
  `rightHip` varchar(100) NOT NULL,
  `leftKnee` varchar(100) NOT NULL,
  `rightKnee` varchar(100) NOT NULL,
  `leftAnkle` varchar(100) NOT NULL,
  `rightAnkle` varchar(100) NOT NULL,
  `patientMeasurement` int(10) NOT NULL,
  `creationDate` timestamp NOT NULL DEFAULT current_timestamp(),
  `updationDate` timestamp NULL DEFAULT NULL ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `manage_users`
--
ALTER TABLE `manage_users`
  ADD PRIMARY KEY (`user_id`);

--
-- Indexes for table `tbldoctor`
--
ALTER TABLE `tbldoctor`
  ADD PRIMARY KEY (`doctorId`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `manage_users`
--
ALTER TABLE `manage_users`
  MODIFY `user_id` int(10) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `tbldoctor`
--
ALTER TABLE `tbldoctor`
  MODIFY `doctorId` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
