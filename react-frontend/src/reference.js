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
        width: "100%",
        maxWidth: 745,
        marginBlock: "20px",
        display: "flex",
        flexDirection: "column",
        justifyContent: "center", // Center vertically
        alignItems: "center", // Center horizontally
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
              style={{
                textDecoration: "none",
                color: "#a248eb",
                fontSize: "18px",
                justifyContent: "center",
                alignItems: "center",
                display: "flex",
                flexDirection: "column",
                textAlign: "center",

                boxSizing: "border-box",
                margin: "0",

                wordWrap: "break-word",
              }}
            >
              Access the data or contribute to this project here:
            </a>
          }
        />
        <CardContent
          sx={{
            display: "flex",
            alignItems: "center",
            justifyContent: "center",
          }}
        >
          <Typography
            variant="body2"
            color="text.secondary"
            style={{
              fontSize: "18px",
              display: "flex",
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