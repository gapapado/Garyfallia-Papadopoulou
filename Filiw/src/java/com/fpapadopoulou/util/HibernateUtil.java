/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.fpapadopoulou.util;

import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.cfg.Configuration;

public class HibernateUtil {
 private static Configuration configuration;
 private static SessionFactory sessionFactory;

 static {
  configuration = new Configuration()
    .configure("com/fpapadopoulou/config/hibernate.cfg.xml");
  sessionFactory = configuration.buildSessionFactory();
 }

 public static Session getSession() {
  Session session = null;
  if (sessionFactory != null) {
   session = sessionFactory.openSession();
  }
  return session;
 }
}