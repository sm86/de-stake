import * as React from "react";
import { useState } from "react";
import { styled } from "@mui/material/styles";
import Card from "@mui/material/Card";
import CardHeader from "@mui/material/CardHeader";
import CardContent from "@mui/material/CardContent";
import CardActions from "@mui/material/CardActions";
import Collapse from "@mui/material/Collapse";
import IconButton from "@mui/material/IconButton";
import Typography from "@mui/material/Typography";
import ExpandMoreIcon from "@mui/icons-material/ExpandMore";
import NewspaperIcon from "@mui/icons-material/Newspaper";

const ExpandMore = styled((props) => {
  const { expand, ...other } = props;
  return <IconButton {...other} />;
})(({ theme, expand }) => ({
  transform: !expand ? "rotate(0deg)" : "rotate(180deg)",
  marginLeft: "auto",
  transition: theme.transitions.create("transform", {
    duration: theme.transitions.duration.shortest,
  }),
}));

function RecipeReviewCard() {
  const [expanded, setExpanded] = React.useState(false);
  const [isHovered, setIsHovered] = useState(false);
  const handleExpandClick = () => {
    setExpanded(!expanded);
  };

  const handlePaperClick = () => {
    window.open("https://arxiv.org/abs/2312.13938", "_blank");
  };
  const handleMouseEnter = () => {
    setIsHovered(true);
  };
  const handleMouseLeave = () => {
    setIsHovered(false);
  };
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
      }}
    >
      <CardHeader
        title={
          <a
            href="https://arxiv.org/abs/2312.13938"
            target="_blank"
            rel="noreferrer"
            style={{
              color: "#a248eb",
              fontSize: "20px",
              justifyContent: "center",
              alignItems: "center",
              display: "flex",
              flexDirection: "column",
              textAlign: "center",
              width: "100%",
              wordWrap: "break-word",
              fontFamily: "Open Sans, Poppins, Montserrat, sans-serif",
              textDecoration: "none",
              fontStyle: "normal",
              textDecorationLine: "none",
              marginLeft: "-15px",
              marginRight: "-15px",
              padding: "0.5rem 1rem",
              borderRadius: "0.25rem",
            }}
          >
            Learn more about the decentralization metrics
          </a>
        }
      />

      <CardContent style={{ marginTop: 0 }}>
        <IconButton
          onMouseEnter={handleMouseEnter}
          onMouseLeave={handleMouseLeave}
        >
          <NewspaperIcon
            className={isHovered ? "hovered" : ""}
            onClick={handlePaperClick}
            style={{
              fontSize: "30px",
              color: "black",
              cursor: "pointer",
            }}
          />
        </IconButton>
      </CardContent>
      <CardActions disableSpacing>
        <ExpandMore
          expand={expanded}
          onClick={handleExpandClick}
          aria-expanded={expanded}
          aria-label="show more"
          style={{ color: "#a248eb", marginTop: "-20px" }}
        >
          <ExpandMoreIcon />
        </ExpandMore>
      </CardActions>
      <Collapse in={expanded} timeout="auto" unmountOnExit>
        <CardContent>
          <Typography
            paragraph
            style={{
              textAlign: "center",
              fontFamily: "Open Sans, Poppins, Montserrat, sans-serif",
              fontStyle: "normal",
            }}
          >
            How Does Stake Distribution Influence Consensus? Analyzing
            Blockchain Decentralization
          </Typography>

          <Typography
            paragraph
            style={{
              textAlign: "justify",
              fontFamily: "Open Sans, Poppins, Montserrat, sans-serif",
              fontStyle: "normal",
            }}
          >
            In the PoS blockchain landscape, the challenge of achieving full
            decentralization is often hindered by a disproportionate
            concentration of staked tokens among a few validators. This study
            analyses this challenge by first formalizing decentralization
            metrics for weighted consensus mechanisms. An empirical analysis
            across ten permissionless blockchains uncovers significant weight
            concentration among validators, underscoring the need for an
            equitable approach. To counter this, we introduce the Square Root
            Stake Weight (SRSW) model, which effectively recalibrates staking
            weight distribution. Our examination of the SRSW model demonstrates
            notable improvements in the decentralization metrics: the Gini index
            improves by 37.16% on average, while Nakamoto coefficients for
            liveness and safety see mean enhancements of 101.04% and 80.09%,
            respectively. This research is a pivotal step toward a more fair and
            equitable distribution of staking weight, advancing the
            decentralization in blockchain consensus mechanisms.
          </Typography>
        </CardContent>
      </Collapse>
    </Card>
  );
}
export default RecipeReviewCard;
