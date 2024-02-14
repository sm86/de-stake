const cardContents = {
    numberOfValidators: {
      title: "Number of validators",
      description:
        "Number of validators participating in the consensus committee.",
      ideal: "Ideal: The higher the better",
    },
    nakomotoSafety: {
        title: "Nakamoto Coefficient Safety",
        description:
          "Percentage of validators to form supermajority, i.e., 66% of network. Can potentially collude to reorg the chain.",
        ideal: "Ideal: The higher the better",
        combined: "Percentage (Absolute Number)",
      },
      nakomotoLiveness: {
        title: "Nakamoto Coefficient Liveness",
        description:
          "Percentage of validators to censor transactions, i.e., 33% of network.",
        ideal: "Ideal: The higher the better",
        combined: "Percentage (Absolute Number)",
      },
    gini: {
      title: "Gini",
      description: "Inequality of stake among the validators in the committee.",
      ideal: "Ideal: The lower the better",
    },
  };
  
  export default cardContents;
  