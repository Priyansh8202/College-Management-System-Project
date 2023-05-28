-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Sep 06, 2022 at 02:41 PM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `shree`
--

-- --------------------------------------------------------

--
-- Table structure for table `adminlogin`
--

CREATE TABLE `adminlogin` (
  `user_id` varchar(50) NOT NULL,
  `PhoneNo` int(12) NOT NULL,
  `Email` varchar(40) NOT NULL,
  `Address` varchar(256) NOT NULL,
  `password` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `fee`
--

CREATE TABLE `fee` (
  `recipt_no` int(20) NOT NULL,
  `student_name` varchar(20) DEFAULT NULL,
  `addmission_number` varchar(20) DEFAULT NULL,
  `total_amount` varchar(20) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `paid_amount` varchar(20) DEFAULT NULL,
  `branch` text DEFAULT NULL,
  `balance` varchar(20) DEFAULT NULL,
  `semster` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `fee`
--

INSERT INTO `fee` (`recipt_no`, `student_name`, `addmission_number`, `total_amount`, `date`, `paid_amount`, `branch`, `balance`, `semster`) VALUES
(1, 'komal', '11', '100', '2022-06-28', '50', 'cs', '50', NULL),
(2, 'dfgd', '6362626', '50000', '2022-09-20', '25000', 'cs', '25000', '6'),
(3, 'iuureiuqew', '6812545', '50000', '2022-07-13', '25000', 'cs', '25000', '2'),
(4, 'arpit', '5225', '20000', '2022-09-23', '10000', 'cs', '10000', '6');

-- --------------------------------------------------------

--
-- Table structure for table `library_management`
--

CREATE TABLE `library_management` (
  `membertype` varchar(30) NOT NULL,
  `bookid` varchar(30) NOT NULL,
  `rollno` varchar(30) NOT NULL,
  `booktitle` varchar(30) NOT NULL,
  `firstname` varchar(30) NOT NULL,
  `lastname` varchar(30) NOT NULL,
  `author` varchar(30) NOT NULL,
  `dateborrowed` date NOT NULL,
  `email` varchar(30) NOT NULL,
  `duedate` date NOT NULL,
  `postcode` varchar(15) NOT NULL,
  `loandays` varchar(5) NOT NULL,
  `mobileno` varchar(10) NOT NULL,
  `bookname` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `library_management`
--

INSERT INTO `library_management` (`membertype`, `bookid`, `rollno`, `booktitle`, `firstname`, `lastname`, `author`, `dateborrowed`, `email`, `duedate`, `postcode`, `loandays`, `mobileno`, `bookname`) VALUES
('Student', 'hjvvhvhh', 'hjvvhjv', 'jhvvv', 'hjvhjvhhv', 'hvhv', 'hvhj', '0005-05-06', 'hvhvjhh', '0005-05-05', 'hhj', 'hvvhv', 'hvjvh', 'Java'),
('Student', 'hvv', 'njh', 'hhh', 'hj', 'hvhj', 'hjv', '0006-04-05', 'hvhvhv', '0006-06-06', 'hjvhjv', 'hvvj', '5454', 'Java');

-- --------------------------------------------------------

--
-- Table structure for table `markdetails`
--

CREATE TABLE `markdetails` (
  `Name` text DEFAULT NULL,
  `father_name` text DEFAULT NULL,
  `mother_name` text DEFAULT NULL,
  `school_name` text DEFAULT NULL,
  `gender` text DEFAULT NULL,
  `date_of_birth` date DEFAULT NULL,
  `roll_no` text NOT NULL,
  `contact_no` int(15) DEFAULT NULL,
  `email_no` varchar(20) DEFAULT NULL,
  `Maths` int(10) NOT NULL,
  `Chemistry` int(10) NOT NULL,
  `Physics` int(10) NOT NULL,
  `Progra` int(10) NOT NULL,
  `English` int(10) NOT NULL,
  `grand_total` int(20) NOT NULL,
  `cgpa` int(20) NOT NULL,
  `result` text NOT NULL,
  `grade` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `markdetails`
--

INSERT INTO `markdetails` (`Name`, `father_name`, `mother_name`, `school_name`, `gender`, `date_of_birth`, `roll_no`, `contact_no`, `email_no`, `Maths`, `Chemistry`, `Physics`, `Progra`, `English`, `grand_total`, `cgpa`, `result`, `grade`) VALUES
('priyansh goel', 'pankaj gupta', 'meeta gupta', 'A V P INTER COLLEGE', 'male', '2022-09-05', '221415435', 2147483647, 'priyanshgoel8202@gma', 52, 13, 12, 32, 34, 0, 0, '', ''),
('arpit', 'fjfs', 'meeta gupta', 'erqwer', 'male', '2022-09-27', '656546168', 351681556, 'priyanshgoel8202@gma', 23, 32, 23, 23, 32, 23, 23, '23', '234');

-- --------------------------------------------------------

--
-- Table structure for table `register form`
--

CREATE TABLE `register form` (
  `Name` text NOT NULL,
  `Middle Name` text NOT NULL,
  `Last Name` text NOT NULL,
  `Course` varchar(10) NOT NULL,
  `Gender` text NOT NULL,
  `Country Code` varchar(5) NOT NULL,
  `Phone No.` varchar(12) NOT NULL,
  `Address` varchar(200) NOT NULL,
  `Password` varchar(15) NOT NULL,
  `Re-Type Password` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `sturegister`
--

CREATE TABLE `sturegister` (
  `rollno` varchar(30) NOT NULL,
  `studentName` varchar(30) NOT NULL,
  `fatherName` varchar(30) NOT NULL,
  `motherName` varchar(30) NOT NULL,
  `DOB` date NOT NULL,
  `address` varchar(100) NOT NULL,
  `city` varchar(30) NOT NULL,
  `mobile` varchar(10) NOT NULL,
  `email` varchar(30) NOT NULL,
  `course` varchar(40) NOT NULL,
  `department` varchar(40) NOT NULL,
  `gender` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `sturegister`
--

INSERT INTO `sturegister` (`rollno`, `studentName`, `fatherName`, `motherName`, `DOB`, `address`, `city`, `mobile`, `email`, `course`, `department`, `gender`) VALUES
('101', 'hjvjh', 'hjvh', 'hj', '0005-05-06', 'hvjh', 'hvjhjv', '5646', 'hjvvh', 'BCA', 'Computer Applications', 'Male');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `fee`
--
ALTER TABLE `fee`
  ADD PRIMARY KEY (`recipt_no`);

--
-- Indexes for table `library_management`
--
ALTER TABLE `library_management`
  ADD PRIMARY KEY (`rollno`);

--
-- Indexes for table `markdetails`
--
ALTER TABLE `markdetails`
  ADD PRIMARY KEY (`roll_no`(15));

--
-- Indexes for table `sturegister`
--
ALTER TABLE `sturegister`
  ADD PRIMARY KEY (`rollno`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
