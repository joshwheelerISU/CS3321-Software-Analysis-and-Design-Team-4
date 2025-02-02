package Backend;

import lombok.Getter;
import lombok.Setter;

public class Chance extends Card {

  //Inspiration from https://github.com/fjricci/monopoly

  /**
   * Constructor
   *
   * @param name     Name of the space
   * @param location The postion on the gameboard
   */
  public Chance(String name, int location, CardType cardType) {
    super(name, location, cardType);
  }

  //variable and field declaration

  /**
   * @param cardNumber Takes in card value
   */
  public void chance(int cardNumber) {
    CardType type = CardType.CHANCE;
    switch (cardNumber) {
      case 0 -> aBoard();
      case 1 -> aGo();
      case 2 -> aIll();
      case 3 -> aCharl();
      //case 4 -> aRail();
      //case 5 -> aUtil();
      case 4 -> dividend();
      //case 7 -> goBack();
      case 5 -> speeding();
      case 6 -> aReading();
      case 7 -> elected();
      case 8 -> loanMature();
      case 9 -> jail();
      case 10 -> jailOut();
      //case 14 -> repairs();
      case 11 -> crosswords();
      default -> {
      }
    }
  }

  private void crosswords() {
    super.setAction(CardAction.ADDMONEY);
    super.setCardDesc("You won a crossword contest! Gain $100.");
    super.setCardValue(100);
  }

  private void loanMature() {
    super.setAction(CardAction.ADDMONEY);
    super.setCardDesc("Your building loan matured. Collect $150.");
    super.setCardValue(150);
  }

  private void elected() {
    super.setAction(CardAction.LOSEMONEY);
    super.setCardDesc("You've been elected to Chairman. Pay each player $50.");
    super.setCardValue(50);
  }

  private void aReading() {
    super.setAction(CardAction.MOVE);
    super.setCardDesc("Advance to reading railroad.");
    super.setCardValue(5);
  }

  private void speeding() {
    super.setAction(CardAction.LOSEMONEY);
    super.setCardDesc("Slow down there, buddy! $15 dollar speeding ticket.");
    super.setCardValue(15);
  }

//  private void goBack() {
//    super.setAction(CardAction.MOVE);
//    super.setCardDesc("Move back 3 spaces.");
//  }

  private void dividend() {
    super.setAction(CardAction.ADDMONEY);
    super.setCardDesc("You received a $50 dollar dividend.");
    super.setCardValue(50);
  }

//  private void repairs() {
//    super.setAction(CardAction.LOSEMONEY);
//    super.setCardDesc("You must repair your property. $25 per house, $100 per hotel.");
//  }
//
//  private void aUtil() {
//    super.setAction(CardAction.MOVE);
//    super.setCardDesc("Advance to the nearest utility.");
//  }

  private void aBoard() {
    super.setAction(CardAction.MOVE);
    super.setCardDesc("Advance to Boardwalk.");
    super.setCardValue(39);
  }

  private void aIll() {
    super.setAction(CardAction.MOVE);
    super.setCardDesc("Advance to Illinois Avenue.");
    super.setCardValue(24);
  }

  private void aCharl() {
    super.setAction(CardAction.MOVE);
    super.setCardDesc("Advance to St. Charles Place.");
    super.setCardValue(11);
  }

//  private void aRail() {
//    super.setAction(CardAction.MOVE);
//    super.setCardDesc("Advance to the nearest railroad.");
//  }

  private void aGo() {
    super.setAction(CardAction.MOVE);
    super.setCardDesc("Travel to Go. Collect $200.");
    super.setCardValue(0);
  }

  private void jail() {
    super.setAction(CardAction.JAIL);
    super.setCardDesc("BONK!!! Straight to horny jail.");
  }

  private void jailOut() {
    super.setAction(CardAction.JAILBREAK);
    super.setCardDesc("MISTRIAL! Get out of jail free.");
  }
}
