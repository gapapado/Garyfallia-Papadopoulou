import java.awt.BorderLayout;
import java.awt.FlowLayout;
import java.awt.GridLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.*;
import java.net.*;
import java.util.ArrayList;
import java.util.Scanner;
import java.util.StringTokenizer;
import javax.swing.JButton;
import javax.swing.JDialog;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JRadioButton;


/**
 * Klasi pou mazevei ta apotelesmata
 * @author 
 */
public class WebCrawler extends JFrame {    
    
    /* ta urls twn syndedriwn*/
    private  static final String[] CONF_URLS = {
           "http://www.informatik.uni-trier.de/~ley/db/conf/sigmod/index.html" , 
           "http://www.informatik.uni-trier.de/~ley/db/conf/pods/index.html" , 
           "http://www.informatik.uni-trier.de/~ley/db/conf/icde/index.html" , 
           "http://www.informatik.uni-trier.de/~ley/db/conf/edbt/index.html" , 
    };
    
    private ArrayList<String>   words;          /* lexeis poy exoun vrethei*/
    private ArrayList<Integer>  wordsCounter;   /* arithmos emfanisewn twn lexewn */

    private String[] sWords;            /* pinakas lexewn taxinomimenos alfavhtika */
    private int[]    sWordsCounter;     /* pinakas metritwn taxinomimenos ws pros tis lexeis */

    private String[] rWords;            /* pinakas lexewn symfwna me ta kritiria */
    private int[]    rWordsCounter;     /* pinakas metritwn symfwna me ta kritiria */
    
    private JRadioButton yearRadio[][]; /* epiloges etwn */
    
    /**
     * Dhmioyrgei ton erpisti
     */
    public WebCrawler() {
        super("Epilogi sendriwn");
        setDefaultCloseOperation(JDialog.DO_NOTHING_ON_CLOSE);
        setResizable(false);
        yearRadio=new JRadioButton[4][12];   
         
        JPanel centerPanel=new JPanel();
        centerPanel.setLayout(new GridLayout(2,2));

        JPanel radioPanel;
        radioPanel=new JPanel();
        radioPanel.setLayout(new GridLayout(3,6));         
        radioPanel.add(new JLabel("SIGMOD"));
        for(int j=0; j<4; j++) {
            String year=2002+j+"";
            yearRadio[0][j]=new JRadioButton(year);
            radioPanel.add(yearRadio[0][j]);
            yearRadio[0][j].setActionCommand("sigmod"+year+".html");
        }
        radioPanel.add(new JLabel(" "));

        radioPanel.add(new JLabel(" "));
        for(int j=0; j<4; j++) {
            String year=2006+j+"";
            yearRadio[0][4+j]=new JRadioButton(year);
            radioPanel.add(yearRadio[0][4+j]);
            yearRadio[0][4+j].setActionCommand("sigmod"+year+".html");
        }
        radioPanel.add(new JLabel(" "));

        radioPanel.add(new JLabel(" "));
        for(int j=0; j<4; j++) {
            String year=2010+j+"";
            yearRadio[0][8+j]=new JRadioButton(year);
            radioPanel.add(yearRadio[0][8+j]);
            yearRadio[0][8+j].setActionCommand("sigmod"+year+".html");
        }
        radioPanel.add(new JLabel(" "));
        
        centerPanel.add(radioPanel);
              
        
        radioPanel=new JPanel();
        radioPanel.setLayout(new GridLayout(3,5));         
        radioPanel.add(new JLabel("PODS"));
        for(int j=0; j<4; j++) {
            String year=2002+j+"";
            yearRadio[1][j]=new JRadioButton(year);
            radioPanel.add(yearRadio[1][j]);
            yearRadio[1][j].setActionCommand("pods"+year+".html");
        }

        radioPanel.add(new JLabel(" "));
        for(int j=0; j<4; j++) {
            String year=2006+j+"";
            yearRadio[1][4+j]=new JRadioButton(year);
            radioPanel.add(yearRadio[1][4+j]);
            yearRadio[1][4+j].setActionCommand("pods"+year+".html");
        }

        radioPanel.add(new JLabel(" "));
        for(int j=0; j<4; j++) {
            String year=2010+j+"";
            yearRadio[1][8+j]=new JRadioButton(year);
            radioPanel.add(yearRadio[1][8+j]);
            yearRadio[1][8+j].setActionCommand("pods"+year+".html");
        }
        centerPanel.add(radioPanel);
        
        radioPanel=new JPanel();
        radioPanel.setLayout(new GridLayout(3,6));         
        radioPanel.add(new JLabel("ICDE"));
        for(int j=0; j<4; j++) {
            String year=2002+j+"";
            yearRadio[2][j]=new JRadioButton(year);
            radioPanel.add(yearRadio[2][j]);
            yearRadio[2][j].setActionCommand("icde"+year+".html");
        }
        radioPanel.add(new JLabel(" "));

        radioPanel.add(new JLabel(" "));
        for(int j=0; j<4; j++) {
            String year=2006+j+"";
            yearRadio[2][4+j]=new JRadioButton(year);
            radioPanel.add(yearRadio[2][4+j]);
            yearRadio[2][4+j].setActionCommand("icde"+year+".html");
        }
        radioPanel.add(new JLabel(" "));

        radioPanel.add(new JLabel(" "));
        for(int j=0; j<4; j++) {
            String year=2010+j+"";
            yearRadio[2][8+j]=new JRadioButton(year);
            radioPanel.add(yearRadio[2][8+j]);
            yearRadio[2][8+j].setActionCommand("icde"+year+".html");
        }
        radioPanel.add(new JLabel(" "));
        centerPanel.add(radioPanel);

        
        radioPanel=new JPanel();
        radioPanel.setLayout(new GridLayout(3,5));         
        radioPanel.add(new JLabel("EDBT"));
        for(int j=0; j<4; j++) {
            String year=2002+j+"";
            yearRadio[3][j]=new JRadioButton(year);
            radioPanel.add(yearRadio[3][j]);
            yearRadio[3][j].setActionCommand("edbt"+year+".html");
        }

        radioPanel.add(new JLabel(" "));
        for(int j=0; j<4; j++) {
            String year=2006+j+"";
            yearRadio[3][4+j]=new JRadioButton(year);
            radioPanel.add(yearRadio[3][4+j]);
            yearRadio[3][4+j].setActionCommand("edbt"+year+".html");
        }

        radioPanel.add(new JLabel(" "));
        for(int j=0; j<4; j++) {
            String year=2010+j+"";
            yearRadio[3][8+j]=new JRadioButton(year);
            radioPanel.add(yearRadio[3][8+j]);
            yearRadio[3][8+j].setActionCommand("edbt"+year+".html");
        }
        centerPanel.add(radioPanel);
        
        JPanel southPanel=new JPanel();
        southPanel.setLayout(new FlowLayout());
        
        JButton okButton=new JButton("Get Results");
        southPanel.add(okButton);
        
        JButton cancelButton=new JButton("Cancel");
        southPanel.add(cancelButton);

        okButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                try {                    
                    search_pages();  /* diavazei ta websites kai ypologizei ta apotelesmata */
                } catch (MalformedURLException ex) {
                    JOptionPane.showMessageDialog(null, "Error url.", "Severe error", JOptionPane.ERROR_MESSAGE);                
                } catch (IOException ex) {
                    JOptionPane.showMessageDialog(null, "Error reading pages.", "Severe error", JOptionPane.ERROR_MESSAGE);                
                }
            }
        });
        
        cancelButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                dispose();  /* kleisimo parathyrou */
            }
        });
        
        
        setLayout(new BorderLayout());
        add(centerPanel, BorderLayout.CENTER);
        add(southPanel, BorderLayout.SOUTH);
        
        pack();
        setVisible(true);                
    }
            
    /**
     * Elegxei an exei epilethei ena synedrio
     * @param conference o arithmos tou synedriou
     * @return true an exei epilexthei, false an oxi
     */
    public boolean isSelected(int conference) {
        for(int j=0; j<12; j++ ) {
            if (yearRadio[conference][j].isSelected()) return true;
        }
        return false;
    }
    
    /* diavazei ta synedria kai metraei tis lexeis */
    private void search_pages() throws MalformedURLException,  IOException {
        words=new ArrayList<String>();
        wordsCounter=new ArrayList<Integer>();
 
        for (int conference=0; conference<4; conference++)  {
            if (! isSelected(conference)) continue;
            String confPage=getFile(CONF_URLS[conference]);    /* diavazei th selida tou synedrioy */
            for (int j=0; j< 12; j++) {      
                if (! yearRadio[conference][j].isSelected()) continue;               
                String year=yearRadio[conference][j].getActionCommand();  
                int pos= confPage.indexOf(year);
                if (pos<0) continue;
                int begin= confPage.lastIndexOf("a href=", pos);
                if (begin<0) continue;
                String articleLink = confPage.substring(begin+8, pos + year.length());  /* vriskei to url tou etous */                                      
                String articlePage=getFile(articleLink);     /* diavazei th selida tou etous */    
                int aTitleStarts= -1;
                int searchFromHere= articlePage.indexOf("ISBN", 0);   
                while( (aTitleStarts=articlePage.indexOf("<span class=\"title\">", searchFromHere)) != -1 ) {
                    int aTitleEnd= articlePage.indexOf("</span>", aTitleStarts);
                    String articleTitle=articlePage.substring(aTitleStarts + 20, aTitleEnd);
                    /* xexorizei tis lexeis tou titlou */
                    StringTokenizer st= new StringTokenizer(articleTitle, " .,:'?()\n\t");
                    while( st.hasMoreTokens() ) {
                        String token= st.nextToken().toLowerCase();
                        pos=words.indexOf(token);
                        if (pos==-1) {
                            words.add(token);   /* h lexh den yparxei sto arraylist, thn vazei me arxiki timi 1 stous metrites */
                            wordsCounter.add(1);
                        } else {
                            int count=wordsCounter.get(pos)+1;  /* auxanei ton arithmo twn lexewn */
                            wordsCounter.set(pos, count);
                        }
                    }
                    searchFromHere= aTitleEnd;    
                }                                                                         
            }                
        }
        sortByCounter();    /* taxinomei kata metriti ta apotelesmata */
        sortByWords();      /* dhmiourgei kai taxinomei alfavhtika ta apotelesmata */
        setVisible(false);
    }
    

    /**
     * Taxinomisi kata metriti
     */
    public void sortByCounter() {
        if (words==null) return;
        int numPairs=words.size();
        String swapString= "";
        Integer swapInt= 0;
        for(int c=0; c<(numPairs-1); c++) {
            for(int d=0; d<numPairs-c-1; d++) {
                if( (int)wordsCounter.get(d) < (int)wordsCounter.get(d+1) ) {   //Descending order            
                    swapInt= wordsCounter.get(d);                   swapString= words.get(d);
                    wordsCounter.set(d, wordsCounter.get(d+1));     words.set(d,words.get(d+1));
                    wordsCounter.set(d+1,swapInt);                  words.set(d+1,swapString);                    
                }
            }
        }        
    }

    /**
     * Taxinomisi kata lexi
     */
     public void sortByWords() {
        if (words==null) return;
        int numPairs=words.size();
        sWords=new String[numPairs];
        sWordsCounter=new int[numPairs];
        
        /* antigrafh twn lexewn stous pinakes gia na taxinomithoun */
        for(int i=0; i<numPairs ; i++) {
            sWords[i]=words.get(i);
            sWordsCounter[i]=wordsCounter.get(i);
        }
        
        String swapString= "";
        int swapInt= 0;
        for(int c=0; c<(numPairs-1); c++) {
            for(int d=0; d<numPairs-c-1; d++) {
                if( sWords[d].compareTo(sWords[d+1])>0 ) {   //Descending order            
                    swapInt= sWordsCounter[d];               swapString= sWords[d];
                    sWordsCounter[d]=sWordsCounter[d+1];     sWords[d]=sWords[d+1];
                    sWordsCounter[d+1]=swapInt;              sWords[d+1]=swapString;                    
                }
            }
        }        
    }
   
    /**
     * Diavazei mia istoselida
     * @param name to url tis selidas
     * @return epistrefei to selida se ena string
     * @throws MalformedURLException
     * @throws IOException 
     */ 
    public String getFile(String name) throws MalformedURLException, IOException {
        URL url=new URL(name);
        URLConnection con = url.openConnection();
        Scanner inp= new Scanner(con.getInputStream());
        String wholeFile="";
        while( inp.hasNextLine() ) wholeFile=wholeFile+inp.nextLine()+"\n";        
        inp.close();         
        return wholeFile;
      }       
    
    /**
     * Filtrarei ta apotelesmata
     * @param minimum_appear o elaxistos arithmos emfanisewn mias lexis
     * @param wordList pinakas lexewn pou apokleiontai
     * @param numberOfResults megistos arithmos apotelesmatwn
     */
    public void setFilters(int minimum_appear, String[] wordList, int numberOfResults) {
        if (words==null) return;
        
        /* proswrina arraylists */
        ArrayList<String>  tmpWords=new ArrayList<String>();            
        ArrayList<Integer> tmpWordsCounter=new ArrayList<Integer>();

        /* filtrarei ta apotelesmat kai dimiourgei ta proswrina arraylists */
        for(int i=0; i<words.size() ; i++) {
            if (wordsCounter.get(i) < minimum_appear) break;

            /* elegxei an h lexh einai apokleismenh */
            boolean found=false;
            for (int j=0; j<wordList.length ; j++) {
                if (wordList[j].equals(words.get(i))) {
                    found=true;
                }
            }
            
            if ( !found ) {
                tmpWords.add(words.get(i));
                tmpWordsCounter.add(wordsCounter.get(i));
                if (numberOfResults !=0 && tmpWords.size()>=numberOfResults) break;
            }                
        }

        /* dhmioyrgei tous telikous pinakes twn filtrarismenwn apotelesmatwn */
        rWords=new String[tmpWords.size()];
        rWordsCounter=new int[tmpWordsCounter.size()];
        for(int i=0; i<tmpWords.size(); i++) {
            rWords[i]=tmpWords.get(i);
            rWordsCounter[i]=tmpWordsCounter.get(i);
        }        
    }

    /**
     * Grafei ola ta apotelesmata se arxeio CSV
     * @param filename to onoma tou arxeiou
     * @throws FileNotFoundException 
     */
    public void writeToCSV(String filename) throws FileNotFoundException {
        PrintWriter out=new PrintWriter(filename);
        for(int i=0; i<sWords.length; i++) {
            out.println(sWords[i]+" , "+sWordsCounter[i]);
        }
        out.close();
    }

    /**
     * accesor
     * @return ton pinaka twn filtrarismenwn lexewn
     */
    public String[] getWords() {
        return rWords;
    }
    
    /**
     * accesor
     * @return ton pinaka twn filtrarismenvn metritwn
     */
    public int[] getWordCounter() {
        return rWordsCounter;
    }
}
