
import java.awt.GridLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.FileNotFoundException;
import javax.swing.JButton;
import javax.swing.JFileChooser;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JMenu;
import javax.swing.JOptionPane;

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 * Vasiko parathyro tis efarmogis
 * @author 
 */
public class ProjectMain extends JFrame implements ActionListener {
    private WebCrawler webCrawler=null;       /* Erpistis */        
               
    /**
     * Dhmiourgei to antikeimeno
     */
    public ProjectMain() {
        super("Statisika synderiwn");
        setDefaultCloseOperation(JFrame.DO_NOTHING_ON_CLOSE);
        this.setResizable(false);
        
        JButton crawlerButton=new JButton("Crawler");             
        JButton chartButton=new JButton("Chart");
        JButton saveButton=new JButton("Save");
        JButton exitButton=new JButton("Exit");

        crawlerButton.setActionCommand("1");
        chartButton.setActionCommand("2");
        saveButton.setActionCommand("3");
        exitButton.setActionCommand("4");
        
        crawlerButton.addActionListener(this);
        chartButton.addActionListener(this);
        saveButton.addActionListener(this);
        exitButton.addActionListener(this);
                
        /* sthsimo twn buttons se morfh grid */
        setLayout(new GridLayout(5,5));
        for(int i=0; i<5; i++) add(new JLabel(" "));
        add(new JLabel(" "));
        add(crawlerButton);
        add(new JLabel(" "));
        add(chartButton);
        add(new JLabel(" "));
        for(int i=0; i<5; i++) add(new JLabel(" "));
        add(new JLabel(" "));
        add(saveButton);
        add(new JLabel(" "));
        add(exitButton);
        add(new JLabel(" "));        
        for(int i=0; i<5; i++) add(new JLabel(" "));
        pack();
        setVisible(true);
    }
        

    /**
     * Trexei tin efarmogi
     * @param args Den exei orismata
     */
    public static void main(String[] args) {
        new ProjectMain();
    }

    @Override
    /* xeirismos twn buttons */
    public void actionPerformed(ActionEvent e) {
        String button=e.getActionCommand();
        switch(button) {
            case "1":  webCrawler=new WebCrawler();     /* psaximo twn sunedriwn */
                       break;
            case "2":  if (webCrawler==null ) break;    /* emfanish barchart */
                       new ChartDialog(webCrawler); 
                       break;
            case "3":  if (webCrawler==null ) break;    /* apothikeusi twn dedomenvn */
                       save_data(); 
                       break;
            case "4":  System.exit(0);                  /* termatismos */
                       break;
        }        
    }

    /* apothikevei ta dedomena se arxeio */
    private void save_data() {
        if (webCrawler==null) return;   /* den exei trexei o erpistis opote den swzei tipota */
	JFileChooser dialog=new JFileChooser(System.getProperty("user.dir"));
        if (dialog.showSaveDialog(this) != JFileChooser.APPROVE_OPTION) return; /* zitaei to onoma kai to fakelo tou arxeiou */

        try {                
            webCrawler.writeToCSV(dialog.getSelectedFile().getAbsolutePath());     
        } 
        catch (FileNotFoundException ex) {
            JOptionPane.showMessageDialog(this, "File not found", "Severe error", JOptionPane.ERROR_MESSAGE);                
        }            
    }
        
}
