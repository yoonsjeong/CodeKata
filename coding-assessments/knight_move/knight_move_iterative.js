function allPossible(n, startRow, startCol) {
  const allMoves = [
    { row: startRow + 2, col: startCol + 1 },
    { row: startRow + 2, col: startCol - 1 },
    { row: startRow - 2, col: startCol + 1 },
    { row: startRow - 2, col: startCol - 1 },
    { row: startRow + 1, col: startCol + 2 },
    { row: startRow + 1, col: startCol - 2 },
    { row: startRow - 1, col: startCol + 2 },
    { row: startRow - 1, col: startCol - 2 },
  ]
  const out = allMoves.filter((am) => {
    const rowValid = am.row < n && am.row >= 0;
    const colValid = am.col < n && am.col >= 0;
    return rowValid && colValid;
  })
  return out;
}

function moveGrid(n, startRow, startCol) {
  if (
    startRow >= n || startRow < 0 ||
    startCol >= n || startCol < 0 ||
    n > 150 || n < 3
  ) {
    throw Error("Out of range.")
  }
  // initialize grid
  const distGrid = new Array(n);
  for (let i = 0; i < distGrid.length; i++) distGrid[i] = new Array(n);
  // start
  distGrid[startRow][startCol] = 0;
  // loop
  let allPoss = allPossible(n, startRow, startCol)
  let moveNum = 1;

  while (true) {
    // discard all squares we've already traveled to
    allPoss = allPoss.filter(ap => distGrid[ap.row][ap.col] === undefined);
    // if we've traveled to all possible moves, we're done.
    if (allPoss.length === 0) break;
    // memoize new coords
    allPoss.forEach(ap => distGrid[ap.row][ap.col] = moveNum)
    // create the next set of possible moves
    const nextSet = []
    allPoss.forEach(ap => {
      const nextPoss = allPossible(n, ap.row, ap.col)
      nextPoss.filter(np =>
        !nextSet.includes(ns => ns.row === np.row && ns.col === np.col)
      )
      nextPoss.forEach(np => {
        nextSet.push({ row: np.row, col: np.col })
      })
    })
    allPoss = nextSet
    moveNum++;
  }
  return distGrid;
}


function minMove(n, startRow, startCol, endRow, endCol) {
  if (
    startRow >= n || startRow < 0 ||
    startCol >= n || startCol < 0 ||
    endRow >= n || endRow < 0 ||
    endCol >= n || endCol < 0 ||
    n > 150 || n < 3
  ) {
    throw Error("Out of range.")
  }

  const grid = moveGrid(n, startRow, startCol);
  return grid[endRow][endCol] || -1;
}

// const print1 = moveGrid(15, 0, 0)
// const print2 = minMove(90, 10, 10, 20, 20);
// console.log(print1);
const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.question("Give grid size: ", gridsize => {
  rl.question("Give startRow: ", startRow => {
    rl.question("Give startCol: ", startCol => {
      try {
        console.log(moveGrid(Number(gridsize), Number(startRow), Number(startCol)))
      }
      catch {
        console.log("Inputs must be non-negative; row & column must be less than grid size.");
      }
      finally {
        rl.close();
      }
    })
  })

});