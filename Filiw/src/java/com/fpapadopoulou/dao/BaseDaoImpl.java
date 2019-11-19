/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.fpapadopoulou.dao;

import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.cfg.Configuration;

import com.fpapadopoulou.pojo.User;
import com.fpapadopoulou.util.HibernateUtil;

public class BaseDaoImpl implements BaseDao {

 @Override
 public boolean login(String username, String password) {
  Session session = HibernateUtil.getSession();
  if (session != null) {
   try {
    User user = (User) session.get(User.class, username);
    if (password.equals(user.getPassword())) {
     System.out.println("User: " + user.toString());
     return true;
    }
   } catch (Exception exception) {
    System.out.println("Exception occred while reading user data: "
      + exception.getMessage());
    return false;
   }

  } else {
   System.out.println("DB server down.....");
  }
  return false;
 }

 @Override
 public String register(User user) {
  String msg = "Registration unsuccessful, try again.....";
  Session session = HibernateUtil.getSession();
  if (session != null) {
   try {
    if (user != null) {
     String username = (String) session.save(user);
     session.beginTransaction().commit();
     msg = "User " + username
       + " created successfully, please login...";
    }
   } catch (Exception exception) {
    System.out.println("Exception occred while reading user data: "
      + exception.getMessage());
   }

  } else {
   System.out.println("DB server down.....");
  }
  System.out.println("msg:" + msg);
  return msg;
 }
}