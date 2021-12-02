/**
 * CSCI1130 Java Assignment 6 BoardGame Reversi
 * Aim: Practise subclassing, method overriding
 *      Learn from other subclass examples
 * 
 * I declare that the assignment here submitted is original
 * except for source material explicitly acknowledged,
 * and that the same or closely related material has not been
 * previously submitted for another course.
 * I also acknowledge that I am aware of University policy and
 * regulations on honesty in academic work, and of the disciplinary
 * guidelines and procedures applicable to breaches of such
 * policy and regulations, as contained in the website.
 *
 * University Guideline on Academic Honesty:
 *   http://www.cuhk.edu.hk/policy/academichonesty
 * Faculty of Engineering Guidelines to Academic Honesty:
 *   https://www.erg.cuhk.edu.hk/erg/AcademicHonesty
 *
 * Student Name: Wong Lap Yin <fill in yourself>
 * Student ID  : 1155147798 <fill in yourself>
 * Date        : 02-12-2021 <fill in yourself>
 */

package boardgame;

import java.awt.Color;
import javax.swing.JButton;
import javax.swing.JOptionPane;

/**
 * Reversi is a TurnBasedGame
 */
public class Reversi extends TurnBasedGame/* TO-DO */ {
    
    public static final String BLANK = " ";
    String winner;
    public boolean[] doPass = new boolean[]{false,false,false,false};

    /*** TO-DO: STUDENT'S WORK HERE ***/
    public Reversi()
    {
        super(8, 8, "BLACK", "WHITE");
        this.setTitle("Reversi");
    }
    
    protected void initGame()
    {
        for (int y = 0; y < yCount; y++)
            for (int x = 0; x < xCount; x++)
                pieces[x][y].setText(" ");
        pieces[3][3].setText("WHITE");
        pieces[3][3].setBackground(Color.WHITE);
        pieces[3][3].setEnabled(false);
        pieces[3][4].setText("BLACK");
        pieces[3][4].setBackground(Color.BLACK);
        pieces[3][4].setEnabled(false);
        pieces[4][3].setText("BLACK");
        pieces[4][3].setBackground(Color.BLACK);
        pieces[4][3].setEnabled(false);
        pieces[4][4].setText("WHITE");
        pieces[4][4].setBackground(Color.WHITE);
        pieces[4][4].setEnabled(false);
        
        
    }
    protected void gameAction(JButton triggeredButton, int x, int y)
    {   
        
        Color animatedColor = currentPlayer.equals("BLACK") ? Color.BLACK : Color.WHITE;
        
        if(isValidMove(x,y)==false)
        {
            System.out.println("Invalid Move!");
            return;
        }
        pieces[x][y].setText(currentPlayer);
        pieces[x][y].setBackground(currentPlayer.equals("BLACK") ? Color.BLACK : Color.WHITE);
        pieces[x][y].setEnabled(false);
        mustPass(x,y);
        /*checkEndGame();
        if (gameEnded)
        {
            addLineToOutput("Game ended!");
            JOptionPane.showMessageDialog(null, "Game ended!");
        }
        else    
            changeTurn();*/
        changeTurn(); // Temp
    }
    public boolean isValidMove(int moveX,int moveY)
    {
        // horizontal check
        boolean returnValue=false;
        if (!pieces[moveX-1][moveY].getText().equals(currentPlayer))
            {
                for(int i=moveX-2;i>=0;i--)
                    {
                        if(pieces[i][moveY].getText().equals(currentPlayer))
                        {
                            doPass[0]=true;
                            returnValue=true;
                        }
                    }
            }
        if(!pieces[moveX+1][moveY].getText().equals(currentPlayer))
        {
            for(int i =moveX+2;i<=7;i++)
            {
                if(pieces[i][moveY].getText().equals(currentPlayer))
                {
                    doPass[0]=true;
                    returnValue=true;
                }
            }
        }
        
        // vertical check
        if(!pieces[moveX][moveY-1].getText().equals(currentPlayer))
        {
            for(int i =moveY-2;i>=0;i--)
            {
                if(pieces[moveX][i].getText().equals(currentPlayer))
                {
                    doPass[1]=true;
                    returnValue=true;
                }
            }
        }
        if(!pieces[moveX][moveY+1].getText().equals(currentPlayer))
        {
            for(int i =moveY+2;i<8;i++)
            {
                if(pieces[moveX][i].getText().equals(currentPlayer))
                {
                    doPass[1]=true;
                    returnValue=true;
                }
            }
        }
        
        // diagonal \ check
        if(!pieces[moveX-1][moveY+1].getText().equals(currentPlayer))
        {
            for(int i=2;(moveX-i>=0)&&(moveY+i<8);i++)
            {
                if(pieces[moveX-i][moveY+i].getText().equals(currentPlayer))
                {
                    doPass[2]=true;
                    returnValue=true;
                }
            }
        }
        if(!pieces[moveX+1][moveY-1].getText().equals(currentPlayer))
        {
            for(int i=2;(moveY-i>=0)&&(moveX+i<8);i++)
            {
                if(pieces[moveX+i][moveY-i].getText().equals(currentPlayer))
                {
                    doPass[2]=true;
                    returnValue=true;
                }
            }
        }
        
        // diagonal / check
        if(!pieces[moveX+1][moveY+1].getText().equals(currentPlayer))
        {
            for(int i =2;moveX+i<8&&moveY+i<8;i++)
            {
                if(pieces[moveX+i][moveY+i].getText().equals(currentPlayer))
                {
                    doPass[3]=true;
                    returnValue=true;
                }
            }
        }
        if(!pieces[moveX-1][moveY-1].getText().equals(currentPlayer))
        {
            for(int i =2;moveX-i>=0&&moveY-i>=0;i++)
            {
                if(pieces[moveX-i][moveY-i].getText().equals(currentPlayer))
                {
                    doPass[3]=true;
                    returnValue=true;
                }
            }
        }
        
        return returnValue;
    }
    protected boolean checkEndGame()
    {
        return true;
    }
    public void countPiece()
    {
        
    }
    public void mustPass(int moveX,int moveY)
    {
        if(doPass[0]==true)
        {
           for(int i=moveX-1;i>=0;i--)
           {
                if(!pieces[i][moveY].getText().equals(currentPlayer)&&!pieces[i][moveY].getText().equals(" "))
                {
                    pieces[i][moveY].setText(currentPlayer);
                    pieces[i][moveY].setBackground(currentPlayer.equals("BLACK") ? Color.BLACK : Color.WHITE);
                }
           }
        
        
            for(int i =moveX+1;i<=7;i++)
            {
                if(!pieces[i][moveY].getText().equals(currentPlayer)&&!pieces[i][moveY].getText().equals(" "))
                {
                    pieces[i][moveY].setText(currentPlayer);
                    pieces[i][moveY].setBackground(currentPlayer.equals("BLACK") ? Color.BLACK : Color.WHITE);
                }
            }
        }
    
        if(doPass[1]==true)
        {
            for(int i =moveY-1;i>=0;i--)
            {
                if(!pieces[moveX][i].getText().equals(currentPlayer)&&!pieces[moveX][i].getText().equals(" "))
                {
                    pieces[moveX][i].setText(currentPlayer);
                    pieces[moveX][i].setBackground(currentPlayer.equals("BLACK") ? Color.BLACK : Color.WHITE);
                }
            }
        
            for(int i =moveY+1;i<8;i++)
            {
                if(!pieces[moveX][i].getText().equals(currentPlayer)&&!pieces[moveX][i].getText().equals(" "))
                {
                    pieces[moveX][i].setText(currentPlayer);
                    pieces[moveX][i].setBackground(currentPlayer.equals("BLACK") ? Color.BLACK : Color.WHITE);
                }
            }
        }
        
        if(doPass[2]==true)
        {
            for(int i=1;(moveX-i>=0)&&(moveY+i<8);i++)
            {
                if(!pieces[moveX-i][moveY+i].getText().equals(currentPlayer)&&!pieces[moveX-i][moveY+i].getText().equals(" "))
                {
                    pieces[moveX-i][moveY+i].setText(currentPlayer);
                    pieces[moveX-i][moveY+i].setBackground(currentPlayer.equals("BLACK")?Color.BLACK:Color.WHITE);
                }
            }
        
        
            for(int i=1;(moveY-i>=0)&&(moveX+i<8);i++)
            {
                if(!pieces[moveX+i][moveY-i].getText().equals(currentPlayer)&&!pieces[moveX-i][moveY+i].getText().equals(" "))
                {
                    pieces[moveX+i][moveY-i].setText(currentPlayer);
                    pieces[moveX+i][moveY-i].setBackground(currentPlayer.equals("BLACK")?Color.BLACK:Color.WHITE);
                }
            }
        
            
        }
        if(doPass[3]==true)
        {
          
            for(int i =1;moveX+i<8&&moveY+i<8;i++)
            {
                if(!pieces[moveX+i][moveY+i].getText().equals(currentPlayer)&&!pieces[moveX+i][moveY+i].getText().equals(" "))
                {
                    pieces[moveX+i][moveY+i].setText(currentPlayer);
                    pieces[moveX+i][moveY+i].setBackground(currentPlayer.equals("BLACK")?Color.BLACK:Color.WHITE);
                }
            }
        
        
            for(int i =2;moveX-i>=0&&moveY-i>=0;i++)
            {
                if(!pieces[moveX-i][moveY-i].getText().equals(currentPlayer)&&!pieces[moveX-i][moveY-i].getText().equals(" "))
                {
                    pieces[moveX-i][moveY-i].setText(currentPlayer);
                    pieces[moveX-i][moveY-i].setBackground(currentPlayer.equals("BLACK")?Color.BLACK:Color.WHITE);
                }
            }
        
        }
    }
    public static void main(String[] args)
    {
        Reversi reversi;
        reversi = new Reversi();
        
        // TO-DO: run other classes, one by one
        System.out.println("You are running class Reversi");
        
        // TO-DO: study comment and code in other given classes
        
        // TO-DO: uncomment these two lines when your work is ready
        reversi.setLocation(400, 20);
        reversi.verbose = false;

        // the game has started and GUI thread will take over here
    }
}
