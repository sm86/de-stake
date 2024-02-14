// MediaCard.js

import React from "react";
import Card from "@mui/material/Card";
import CardContent from "@mui/material/CardContent";
import Button from "@mui/material/Button";
import Typography from "@mui/material/Typography";
import { useState, useEffect } from "react";

function MediaCard({ position, content }) {
  const [cardPosition, setCardPosition] = useState({ x: 0, y: 0 });

  useEffect(() => {
    const cardWidth = 300; 
    const cardHeight = 200; 
    const viewportWidth = window.innerWidth;
    const viewportHeight = window.innerHeight;

    let newX = position.x + 20; 
    let newY = position.y + 20;

    if (newX + cardWidth > viewportWidth) {
      newX = viewportWidth - cardWidth - 20; 
    }

    
    if (newY + cardHeight > viewportHeight) {
      newY = viewportHeight - cardHeight - 20;
    }

    setCardPosition({ x: newX, y: newY });
  }, [position]);

  return (
    <Card
      sx={{
        maxWidth: 300,
        position: "absolute",
        top: cardPosition.y,
        left: cardPosition.x,
      }}
    >
      <CardContent>
        <div
          style={{
            backgroundColor: "#a248eb",
            padding: "10px",
            marginBottom: "10px",
          }}
        >
          <Typography variant="body2" color="text.secondary">
            <span
              style={{
                fontFamily: "Baskerville",
                fontSize: content.title.length < 25 ? "20px" : "17px",
                fontWeight: "bold",
                marginRight: "5px",
                color: "white",
              }}
            >
              {content.title}
            </span>{" "}
            <br />
            <span
              style={{
                fontFamily: "Baskerville",
                marginRight: "5px",
                color: "white",
              }}
            >
              {content.combined}
              <br />
            </span>
            <span
              style={{
                fontFamily: "Baskerville",
                marginRight: "5px",
                color: "white",
              }}
            >
              {content.ideal}
            </span>
          </Typography>
        </div>
        <div style={{ padding: "10px", wordWrap: "break-word" }}>
          <Typography
            variant="body2"
            style={{ fontFamily: "Baskerville", color: "black" }}
          >
            {content.description}
          </Typography>
        </div>
      </CardContent>
      <div
        style={{
          display: "flex",
          justifyContent: "flex-end",
          paddingRight: "16px",
        }}
      ></div>
    </Card>
  );
}

export default MediaCard;