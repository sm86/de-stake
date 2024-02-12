import * as React from "react";
import { styled } from "@mui/material/styles";
import Card from "@mui/material/Card";
import CardHeader from "@mui/material/CardHeader";
import CardMedia from "@mui/material/CardMedia";
import CardContent from "@mui/material/CardContent";
import CardActions from "@mui/material/CardActions";
import Collapse from "@mui/material/Collapse";
import Avatar from "@mui/material/Avatar";
import IconButton from "@mui/material/IconButton";
import Typography from "@mui/material/Typography";
import { red } from "@mui/material/colors";
import FavoriteIcon from "@mui/icons-material/Favorite";
import ShareIcon from "@mui/icons-material/Share";
import CopyIcon from "@mui/icons-material/FileCopy";
import ExpandMoreIcon from "@mui/icons-material/ExpandMore";
import MoreVertIcon from "@mui/icons-material/MoreVert";

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

  const handleExpandClick = () => {
    setExpanded(!expanded);
  };

  return (
    <Card sx={{ maxWidth: 745, marginBlock: "20px" }}>
      <CardHeader
        // avatar={
        //   <Avatar sx={{ bgcolor: red[500] }} aria-label="recipe">

        //   </Avatar>
        // }

        // action={
        //   <IconButton aria-label="settings">
        //     <MoreVertIcon />
        //   </IconButton>
        // }
        title={
          <a
            href="https://arxiv.org/abs/2312.13938"
            target="_blank"
            style={{
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
            Learn more about the decentralization metrics
          </a>
        }
        // subheader="21 Dec 2023"
      />

      <CardContent>
        <Typography
          variant="body2"
          color="text.secondary"
          style={{
            justifyContent: "center",
            alignItems: "center",
          }}
        >
          How Does Stake Distribution Influence Consensus? Analyzing Blockchain
          Decentralization{" "}
          <a
            href="https://arxiv.org/search/cs?searchtype=author&query=Motepalli,+S"
            target="_blank"
            style={{ color: "#a248eb" }}
          >
            Shashank Motepalli
          </a>
          ,{" "}
          <a
            href="https://arxiv.org/search/cs?searchtype=author&query=Jacobsen,+H"
            target="_blank"
            style={{ color: "#a248eb" }}
          >
            Hans-Arno Jacobsen
          </a>
        </Typography>
      </CardContent>
      <CardActions disableSpacing>
        {/* <IconButton aria-label="add to favorites">
          <FavoriteIcon />
        </IconButton> */}
        {/* <IconButton aria-label="share">
          <ShareIcon />
          <CopyIcon />
        </IconButton> */}
        <ExpandMore
          expand={expanded}
          onClick={handleExpandClick}
          aria-expanded={expanded}
          aria-label="show more"
        >
          <ExpandMoreIcon />
        </ExpandMore>
      </CardActions>
      <Collapse in={expanded} timeout="auto" unmountOnExit>
        <CardContent>
          <Typography paragraph>
            How Does Stake Distribution Influence Consensus? Analyzing
            Blockchain Decentralization
          </Typography>

          <Typography paragraph style={{ textAlign: "justify" }}>
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
