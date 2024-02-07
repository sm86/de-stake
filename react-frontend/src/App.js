import React, { useState, useEffect } from "react";
import "./App.css";

const App = () => {
  const [tableData, setTableData] = useState([]);
  const [selectedDate, setSelectedDate] = useState(getYesterdayDate());
  const [value, setValue] = useState(null); 

  // eslint-disable-next-line react-hooks/exhaustive-deps
  useEffect(() => {
    fetchData();
  }, [selectedDate]);

  useEffect(() => {
    setValue(handleDatePicker());
  }, []);


  const fetchData = () => {
    if (!selectedDate) {
      console.error("Please select a date.");
      return;
    }
    let domain = window.location.origin;
    let port = 5000;
    let url = `${domain}:${port}/metrics/${selectedDate}`;
    fetch(url)
      .then((response) => response.json())
      .then((data) => {
        console.log("Data fetched:", data);
        setTableData(data);
      })
      .catch((error) =>
        console.error(
          "No data available for the selected date. Please select a valid date.",
          error
        )
      );
  };

  const handleDatePicker = () => {
    const currentDate = new Date();
    const day = currentDate.getDate() - 1;
    const month = currentDate.getMonth() + 1;
    const year = currentDate.getFullYear();
    return `${year}-${month < 10 ? "0" + month : month}-${
      day < 10 ? "0" + day : day
    }`;
  }

  const handleDateChange = (e) => {
    const inputDate = new Date(e.target.value + "T00:00:00");
    inputDate.setHours(0, 0, 0, 0);
    const day = inputDate.getDate().toString().padStart(2, "0");
    const month = (inputDate.getMonth() + 1).toString().padStart(2, "0");
    const year = inputDate.getFullYear().toString();
    const formattedDate = day + month + year;
    setSelectedDate(formattedDate);
    setValue(e.target.value);
  };

  const handleYesterdayDate = () => {
    const currentDate = new Date();
    const day = currentDate.getDate() - 1;
    const month = currentDate.getMonth() + 1;
    const year = currentDate.getFullYear();
    return `${day < 10 ? "0" + day : day}-${
      month < 10 ? "0" + month : month
    }-${year}`;
  };

  function getYesterdayDate() {
    const yesterday = new Date();
    yesterday.setDate(yesterday.getDate() - 1);

    const day = yesterday.getDate().toString().padStart(2, "0");
    const month = (yesterday.getMonth() + 1).toString().padStart(2, "0");
    const year = yesterday.getFullYear().toString();

    return day + month + year;
  }

  function capitalizeFirstLetter(string) {
    return string.charAt(0).toUpperCase() + string.slice(1);
  }

  return (
    <div className="app-container">
      <header className="header">Decentralization in PoS Blockchains</header>

      {selectedDate ? (
        <div className="metrics-section">
          <table className="metrics-table">
            {tableData && tableData.length > 0 ? (
              <>
                <thead>
                  <tr>
                    <th>Blockchain</th>
                    <th>Number of validators</th>
                    <th>Nakamoto Coefficient Safety</th>
                    <th>Nakamoto coefficient Liveness</th>
                    <th>Gini</th>
                  </tr>
                </thead>
                <tbody>
                  {tableData.map((item, index) => (
                    <tr key={index}>
                      <td>{capitalizeFirstLetter(item.blockchain)}</td>
                      <td>{item.N}</td>
                      <td>
                        {item.nc_safety_percent}% ({item.nc_safety})
                      </td>
                      <td>
                        {item.nc_liveness_percent}% ({item.nc_liveness})
                      </td>
                      <td>{item.gini}</td>
                    </tr>
                  ))}
                </tbody>
              </>
            ) : (
              <div>
                <h3 className="no-data">
                  No data available for the selected date. Please select a date
                  between 24-10-2023 and {handleYesterdayDate()}
                </h3>
              </div>
            )}
          </table>
        </div>
      ) : (
        <div>
          <h3 className="no-data"> Please select a date</h3>
        </div>
      )}
      <div className="centered-content">
        <div className="date-selection">
          <label htmlFor="datePicker">Please select a date</label>
          <input
            className="date-picker"
            type="date"
            id="datePicker"
            value= {value}
            onChange={handleDateChange}
          />
        </div>
      </div>
      <div className="pdf-label centered-content">
        <label>Reference:</label>
        <a
          href="https://arxiv.org/abs/2312.13938"
          className="pdf-link"
          target="_blank"
          rel="noopener noreferrer"
        >
          Analyzing Blockchain Decentralization
        </a>
      </div>

      <footer className="footer">
  <a
    className="footerlink"
    href="https://github.com/sm86"
    target="_blank"
    rel="noopener noreferrer"
  >
    <i className="fab fa-github"></i>
  </a>
  <a
    className="footerlink"
    href="https://twitter.com/sh1sh1nk?lang=en"
    target="_blank"
    rel="noopener noreferrer"
  >
    <i className="fab fa-twitter"></i> 
  </a>
  <a
    className="footerlink"
    href="https://www.linkedin.com/in/smotepalli?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app"
    target="_blank"
    rel="noopener noreferrer"
  >
    <i className="fab fa-linkedin"></i> 
  </a>
</footer>
    </div>
  );
};

export default App;
