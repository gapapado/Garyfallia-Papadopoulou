
import java.awt.BorderLayout;
import java.awt.FlowLayout;
import java.awt.GridLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.StringTokenizer;
import javax.swing.ButtonGroup;
import javax.swing.JButton;
import javax.swing.JComboBox;
import javax.swing.JDialog;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JRadioButton;
import javax.swing.JTextField;

/**
 * Parathyro dialogou me to xrisi gia ton kathorismo twn filtrwn emfanisis tou grafimatos
 * @author
 */
public class ChartDialog extends JFrame {
    private static final String[] CHOICES_TXT={"0","2","4","6","8","10","12","14","16","18","20","22","24","26","28","30"};  /* gia to combobox */
    private static final int[] CHOICES={0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30};  /* gia tous arihmous */

    private JComboBox minimumCombo=new JComboBox(CHOICES_TXT); /* elaxistos arithmos emfanisis apotelesmatwn */
    private JTextField wordField;   /* lexeis poy apokleiontai */
    private JButton okButton=new JButton("OK");
    private JRadioButton top1,top5,top10,top50,top100,topAll;   /* epiloges plithous apotelesmatwn */
    private WebCrawler webCrawler;     /* erpistis */

    /**
     * Dhmiourgei to parathryro
     * @param webCrawler o eripistis gia ton opoio tha emfanisei ta apotelesmata
     */
    public ChartDialog(WebCrawler webCrawler) {
        super("Epiloges grafimatos");
        setDefaultCloseOperation(JDialog.DISPOSE_ON_CLOSE);
        setSize(550, 170);
        setResizable(false);
        this.webCrawler=webCrawler;
        
        setLayout(new BorderLayout());
        JPanel selectionsPanel=new JPanel();
        JPanel radioPanel=new JPanel();

        selectionsPanel.setLayout(new FlowLayout());
            
        selectionsPanel.add(new JLabel("Min. appear.: "));
        minimumCombo.setSelectedIndex(0);
        selectionsPanel.add(minimumCombo);
       
        selectionsPanel.setLayout(new FlowLayout());
        selectionsPanel.add(new JLabel("Exclude: "));      
        wordField=new JTextField(30);
        selectionsPanel.add(wordField);
            
        selectionsPanel.add(new JLabel("Totals : "));      
        
        radioPanel.setLayout(new GridLayout(2,3));
        ButtonGroup topGroup=new ButtonGroup();
        top1=new JRadioButton("top-1");
        top5=new JRadioButton("top-5");
        top10=new JRadioButton("top-10");
        top50=new JRadioButton("top-50");
        top100=new JRadioButton("top-100");
        topAll=new JRadioButton("All");
        topAll.setSelected(true);

        radioPanel.add(top1);
        radioPanel.add(top5);
        radioPanel.add(top10);
        radioPanel.add(top50);
        radioPanel.add(top100);
        radioPanel.add(topAll);
       
        topGroup.add(top1);            
        topGroup.add(top5);            
        topGroup.add(top10);            
        topGroup.add(top50);            
        topGroup.add(top100);            
        topGroup.add(topAll);            
        selectionsPanel.add(radioPanel);
           
        radioPanel.setLayout(new FlowLayout());
        okButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                createChart();  /* dhmioyrgei to grafima */
            }
        });

        JPanel buttonPanel=new JPanel();
        buttonPanel.add(okButton);
            
        add(selectionsPanel,BorderLayout.CENTER);
        add(buttonPanel,BorderLayout.SOUTH);
          
        setVisible(true);             
    }

    /**
     * Dhmiourgei to grafima
     */
    public void createChart() {
        int numberOfResults;
        int minimum_appear;
        String[] wordList;

        /* pairnei ta kritiria apo to xristi */
        int pos=minimumCombo.getSelectedIndex();
        minimum_appear=CHOICES[pos];
                
        StringTokenizer st= new StringTokenizer(wordField.getText(), " ,:'?()\n\t");
        int total=st.countTokens();
        wordList = new String[total];
        for (int i=0; i<total; i++ ) { 
            wordList[i]=st.nextToken().toLowerCase();
        }
        if (top1.isSelected()) numberOfResults=1; 
        else if (top5.isSelected()) numberOfResults=5; 
        else if (top10.isSelected()) numberOfResults=10; 
        else if (top50.isSelected()) numberOfResults=50; 
        else if (top100.isSelected()) numberOfResults=100; 
        else  numberOfResults=0;
            
        webCrawler.setFilters(minimum_appear, wordList, numberOfResults);       /* efarmozei ta kritiria ston erpisti */
        new ChartFrame(webCrawler.getWords(), webCrawler.getWordCounter());     /* emfanizei to grafhma */
        dispose();
    }                    
}
