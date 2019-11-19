/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.fpapadopoulou.pojo;

public class User {
 private String name;
 private String password;
 private String email;

 public String getName() {
  return name;
 }

 public void setName(String username) {
  this.name = username;
 }

 public String getPassword() {
  return password;
 }

 public void setPassword(String password) {
  this.password = password;
 }



 public String getEmail() {
  return email;
 }

 public void setEmail(String emailId) {
  this.email = emailId;
 }

 @Override
 public String toString() {
  return "User [username=" + name + ", password=" + password
    + ", emailId=" + email + "]";
 }
}