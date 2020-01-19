
const getUserChoice = userInput => {
  userInput = userInput.toLowerCase();
  if (userInput === 'rock' || userInput === 'paper' || userInput === 'scissors') {
    return userInput;
  } else {
    console.log('Ooops, that is an error!');
  }
}
// tested and it worked with some debugging
// console.log(getUserChoice('SCISSORS'))

const getComputerChoice = () => {
  const randomNumber = Math.floor(Math.random() * 3)
  switch (randomNumber) {
    case 0:
      return 'rock';
    case 1:
      return 'paper';
    case 2:
      return 'scissors';
  }
};
// test getComputerChoice function -- works
// console.log(getComputerChoice());

const determineWinner = (userChoice, computerChoice) => {
  if (userChoice === computerChoice) {
    return 'The game was a tie';
 }
  if (userChoice === 'rock') {
    if (computerChoice === 'paper') {
      return 'The computer won!';
    } else {
      return 'You won!';
    }
 }
  if (userChoice === 'paper') {
    if (computerChoice === 'scissors') {
      return 'The computer won!';
    }
  else {
    return 'You won!';
  }
 } else if (userChoice === 'scissors') {
    if (computerChoice === 'rock'){
      return 'The computer won!';
    } else {
      return 'You won!'
    }
  }
};

const playGame = () => {
  const userChoice = getUserChoice('scissors');
  const computerChoice = getComputerChoice();
  console.log('You threw: ' + userChoice)
  console.log('Computer threw: ' + computerChoice);
  console.log(determineWinner(userChoice, computerChoice));
};
playGame('scissors', getComputerChoice());
