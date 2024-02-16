import React, { useState, useEffect } from "react";
import "./App.css";
import MediaCard from "./card.js";
import cardContents from "./cardContents.js";
import ActionAreaCard from "./reference.js";
import RecipeReviewCard from "./paper.js";

const App = () => {
  const [tableData, setTableData] = useState([]);
  const [selectedDate, setSelectedDate] = useState(getYesterdayDate());
  const [value, setValue] = useState(null);
  const [showCard, setShowCard] = useState(false);
  const [position, setPosition] = useState({ x: 0, y: 0 });
  const [currentHeading, setCurrentHeading] = useState(null);
  // Function to handle mouse over
  const handleMouseOver = (e, heading) => {
    const rect = e.target.getBoundingClientRect();
    setPosition({
      x: rect.left + window.scrollX,
      y: rect.top + window.scrollY,
    });
    setCurrentHeading(heading);
    setShowCard(true);
  };

  const handleMouseOut = () => {
    setShowCard(false);
  };

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
    // let port = 5000;
    // let url = `${domain}:${port}/metrics/${selectedDate}`;
    let url = `${domain}/metrics/${selectedDate}`;
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
    <div className="app-container"style={{
      fontFamily: "Open Sans, Poppins, Montserrat, sans-serif",
    }} >
      <header className="header">Is your Blockchain Decentralized?</header> 

      {selectedDate ? (
        <div className="metrics-section">
          <table className="metrics-table">
            {tableData && tableData.length > 0 ? (
              <>
                 <thead>
                  <tr>
                    <th>Blockchain</th>
                    <th>
                      Number of validators
                      <span
                        className="info"
                        onMouseOver={(e) =>
                          handleMouseOver(e, "numberOfValidators")
                        }
                        onMouseOut={handleMouseOut}
                      >
                        {" "}
                        &nbsp;
                        <i class="fa fa-info-circle"></i>
                      </span>
                    </th>
                    <th>
                      Nakamoto Coefficient Safety
                      <span
                        className="info"
                        onMouseOver={(e) =>
                          handleMouseOver(e, "nakomotoSafety")
                        }
                        onMouseOut={handleMouseOut}
                      >
                        {" "}
                        &nbsp;
                        <i class="fa fa-info-circle" aria-hidden="true"></i>
                      </span>
                    </th>
                    <th>
                      Nakamoto coefficient Liveness
                      <span
                        className="info"
                        onMouseOver={(e) =>
                          handleMouseOver(e, "nakomotoLiveness")
                        }
                        onMouseOut={handleMouseOut}
                      >
                        {" "}
                        &nbsp;
                        <i class="fa fa-info-circle" aria-hidden="true"></i>
                      </span>
                    </th>
                    <th>
                      Gini
                      <span
                        className="info"
                        onMouseOver={(e) => handleMouseOver(e, "gini")}
                        onMouseOut={handleMouseOut}
                      >
                        {" "}
                        &nbsp;
                        <i class="fa fa-info-circle" aria-hidden="true"></i>
                      </span>
                    </th>
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
          {showCard && (
            <MediaCard
              position={position}
              content={cardContents[currentHeading]}
            />
          )}
        </div>
      ) : (
        <div>
          <h3 className="no-data"> Please select a date</h3>
        </div>
      )}
      <div className="centered-content">
        <div className="date-selection">
          <label
            htmlFor="datePicker"
            Style={{ marginRight: "10px", fontFamily: "Open Sans, Poppins, Montserrat, sans-serif" }}
          >
            You are viewing metrics as of
          </label>
          <input
            className="date-picker"
            type="date"
            id="datePicker"
            value={value}
            onChange={handleDateChange}
          />
        </div>
      </div>

      <div className=" centered-content">
        <RecipeReviewCard />
        <ActionAreaCard />
      </div>

      <footer className="footer" style={{ fontSize: "20px", fontFamily: "Open Sans, Poppins, Montserrat, sans-serif" }}>
        <label htmlFor="footerlink">Connect with us:</label>
        <a
          className="pdf-link"
          href="https://twitter.com/sh1sh1nk?lang=en"
          target="_blank"
          rel="noopener noreferrer"
          style={{
            textDecoration: "none",
            display: "inline-flex",
            alignItems: "center",
            marginLeft: "-15px",
          }}
        >
          <i
            className="fab fa-twitter"
            style={{ marginRight: "3px", marginBottom: "2px" }}
          ></i>
          @sh1sh1nk
        </a>
      </footer>
    </div>
  );
};

export default App;
