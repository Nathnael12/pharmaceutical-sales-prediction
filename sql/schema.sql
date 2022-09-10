CREATE TABLE IF NOT EXISTS `SalesFeatures` (
  `Store` INT NOT NULL ,
  `DayOfWeek` INT NOT NULL,
  `Date` VARCHAR(200) NOT NULL,
  `Sales` INT DEFAULT NULL,
  `Customers` INT DEFAULT NULL,  
  `Open` INT DEFAULT NULL,
  `Promo` INT DEFAULT NULL,
  `StateHoliday` INT DEFAULT NULL,
  `SchoolHoliday` INT DEFAULT NULL,
  `StoreType` INT DEFAULT NULL,
  `Assortment` INT DEFAULT NULL,
  `CompetitionDistance` FLOAT DEFAULT NULL,
  `CompetitionOpenSinceMonth` FLOAT DEFAULT NULL,
  `CompetitionOpenSinceYear` FLOAT DEFAULT NULL,
  `Promo2` INT DEFAULT NULL,
  `Promo2SinceWeek` FLOAT DEFAULT NULL,
  `PromoInterval` INT DEFAULT NULL,
  `Weekday` INT DEFAULT NULL,
  `Weekend` INT DEFAULT NULL,
  `Month` INT DEFAULT NULL,
  `Year` INT DEFAULT NULL,
  `Day` INT DEFAULT NULL,
  `PeriodInMonth` INT DEFAULT NULL,
  `Before_holiday` INT DEFAULT NULL,
  `After_holiday` INT DEFAULT NULL,
  PRIMARY KEY (`Store`)
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE utf8mb4_unicode_ci;