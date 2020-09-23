
import java.awt.Color;
import java.awt.Graphics;
import javax.swing.JFrame;

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 * Dimiourgei ena grafhma me orizontia bars
 * @author 
 */
public class ChartFrame extends JFrame {        
    private String[] words;
    private int[] counters;
        
    /**
     * Dimiourgei to antikeimeno
     * @param words o pinakas me tis lexeis
     * @param counters o pinakas me toys metrites
     */
    public ChartFrame(String[] words, int[] counters ) {             
        super("Grafima"); 
        this.words=words;
        this.counters=counters;
        this.setDefaultCloseOperation(DISPOSE_ON_CLOSE);
        this.setSize(800, 600);
        this.setVisible(true);
    }

    /**
     * Zwgrafizei to grafima
     * @param g graphics object
     */
    public void paint(Graphics g) {
        super.paint(g);        
        if (words.length==0 || counters.length==0) {
            g.drawString("Nothing to display", 100, 100);
            return;
        }
        int xw=10;      /* orizontia arxh twn lexewn */ 
        int xc=xw+100;  /* orizontia arxh ths mparas */
        int y=50;       /* arxh tou kathetou axona */
        int w=20;       /* platos mparas */
        int max=counters[0];
        for(int i=0; i<words.length; ++i) {
            if (i%20==0 && i>0) {   /* kathe 20 lexeis dhmioyrgei to grafhma se nea perioxh sto frame */
                xw=xc+max+10+50;
                xc=xw+100;
                max=counters[i];
                y=50;
            }
            g.setColor(Color.black);
            g.drawString(words[i], xw, y+(3*w)/4);  /* grafei tis lexeis */
            g.setColor(Color.MAGENTA);
            g.fillRect(xc, y, counters[i], w);      /* kanei th mpara */
            g.setColor(Color.black);
            g.drawString(counters[i]+"", xc+counters[i]+10, y+(3*w)/4); /* grafei to metriti */
            y=y+(5*w)/4;            
        }        
    }
}

