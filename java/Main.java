package org.example;

import java.io.File;
import java.io.FileNotFoundException;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;
import java.util.Scanner;
import com.google.gson.JsonArray;
import com.google.gson.Gson;
import com.google.gson.JsonElement;
import com.google.gson.JsonObject;

public class Main {
    public static void main(String[] args) {
        String url = "jdbc:mysql://mysql.hinoob.xyz:3306/s5_aastategija";
        String username = "CENSORED";
        String password = "CENSORED";

        try {
            Class.forName("com.mysql.jdbc.Driver");
            Connection connection = DriverManager.getConnection(url, username, password);
            System.out.println("Connected to the database!");

            File file = new File("v.txt");
            if(file.exists()) {
                System.out.println("FOUND");
                try {
                    Scanner scanner = new Scanner(file);
                    StringBuilder jsonStringBuilder = new StringBuilder();
                    while (scanner.hasNextLine()) {
                        jsonStringBuilder.append(scanner.nextLine());
                    }
                    String jsonData = jsonStringBuilder.toString();
                    JsonArray array = new Gson().fromJson(jsonData, JsonArray.class);
                    for(JsonElement element : array.asList()) {
                        JsonObject object = element.getAsJsonObject();
                        String nimi = object.get("title").getAsString();
                        int aasta = Integer.parseInt(object.get("description").getAsJsonArray().get(0).getAsString());
                        String labisoit = object.get("description").getAsJsonArray().get(1).getAsString();
                        String kutus = object.get("description").getAsJsonArray().get(2).getAsString();
                        String kaigukast = object.get("description").getAsJsonArray().get(3).getAsString();
                        String kere = object.get("description").getAsJsonArray().get(4).getAsString();
                        String tyyp = object.get("description").getAsJsonArray().get(5).getAsString();

                        String query = "INSERT INTO soidukid (`nimi`, `aasta`, `labisoit`, `kutus`, `tüüp`, `kere`, `käigukast`, `pilt`) VALUES (?, ?, ?, ?, ?, ?, ?, ?)";

                        PreparedStatement preparedStatement = connection.prepareStatement(query);
                        preparedStatement.setString(1, nimi); 
                        preparedStatement.setInt(2, aasta);
                        preparedStatement.setString(3, labisoit);
                        preparedStatement.setString(4, kutus); 
                        preparedStatement.setString(5, tyyp); 
                        preparedStatement.setString(6, kere); 
                        preparedStatement.setString(7, kaigukast); 
                        preparedStatement.setString(8, object.get("image").getAsString());

                        preparedStatement.executeUpdate();

                    }
                    
                    scanner.close();
                } catch (FileNotFoundException e) {
                    e.printStackTrace();
                }
            }
            
            connection.close();
        } catch (SQLException e) {
            // Handle any SQL exceptions
            e.printStackTrace();
        } catch (ClassNotFoundException e) {
            throw new RuntimeException(e);
        }
    }
}
