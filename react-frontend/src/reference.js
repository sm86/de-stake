import * as React from "react";
import Card from "@mui/material/Card";
import CardContent from "@mui/material/CardContent";
import CardMedia from "@mui/material/CardMedia";
import Typography from "@mui/material/Typography";
import CardHeader from "@mui/material/CardHeader";
import { CardActionArea } from "@mui/material";

function ActionAreaCard() {
  return (
    <Card
      sx={{
        maxWidth: 745,
        marginBlock: "20px",
        alignItems: "center",
        justifyContent: "center",
        display: "flex",
        flexDirection: "column",
        borderRadius: "0.25rem",
        boxShadow: "0 0.5rem 1rem 0 rgba(0, 0, 0, 0.1)",
        width: "100%",
        height: "100%",
      }}
    >
      <CardActionArea
        onClick={() => window.open("https://github.com/sm86/destake", "_blank")}
      >
        <CardMedia />
        <CardHeader
          title={
            <a
              href="https://github.com/sm86/destake"
              target="_blank"
              rel="noreferrer"
              style={{
                textDecoration: "none",
                color: "#a248eb",
                fontSize: "20px",
                justifyContent: "center",
                alignItems: "center",
                display: "flex",
                flexDirection: "column",
                textAlign: "center",
                wordWrap: "break-word",
                fontFamily: "Open Sans, Poppins, Montserrat, sans-serif",
                boxSizing: "border-box",
                margin: "0",
            }}
            >
              Access the data or contribute to this project here
            </a>
          }
        />
        <CardContent
          sx={{
            display: "flex",
            alignItems: "center",
            justifyContent: "center",
            flexDirection: "column",
            padding: "20px 0 20px 0",
            textAlign: "center",
            width: "100%",
            height: "100%",
            borderRadius: "0 0 0.25rem 0.25rem",
            fontFamily: "Open Sans, Poppins, Montserrat, sans-serif",
          }}
        >
          <Typography
            variant="body2"
            color="text.secondary"
            style={{
              display: "flex",
              justifyContent: "center",
              flexDirection: "column",
              textAlign: "center",
              alignItems: "center",
            }}
          >
            <i
              className="fab fa-github"
              style={{ fontSize: "22px", marginRight: "5px", color: "black" }}
            ></i>
            <a
              href="https://github.com/sm86/destake"
              className=""
              target="_blank"
              rel="noopener noreferrer"
              style={{
                textDecoration: "none",
                color: "black",
                fontSize: "18x",
              }}
            >
              Github
            </a>
          </Typography>
        </CardContent>
      </CardActionArea>
    </Card>
  );
}

export default ActionAreaCard;