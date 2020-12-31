package com.macht.amanda;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import com.google.android.gms.tasks.OnFailureListener;
import com.google.android.gms.tasks.OnSuccessListener;
import com.google.firebase.auth.AuthResult;
import com.google.firebase.auth.FirebaseAuth;

public class MainActivity extends AppCompatActivity {
    EditText Email,Password;
    Button SigninButton;
    FirebaseAuth firebaseAuth;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        Email = findViewById(R.id.emailsignin);
        Password = findViewById(R.id.passwordsignin);
        SigninButton = findViewById(R.id.signinbutton);
        firebaseAuth = FirebaseAuth.getInstance();

        if (firebaseAuth.getCurrentUser()!=null){
            startActivity(new Intent(MainActivity.this,HomeActivity.class));
            finish();
        }

        SigninButton.setOnClickListener(v -> {
            String email = Email.getText().toString().trim();
            String password = Password.getText().toString().trim();

            if(email.isEmpty()||password.isEmpty()){
                Toast.makeText(this, "Empty Fields", Toast.LENGTH_SHORT).show();
            }else{
                firebaseAuth.signInWithEmailAndPassword(email,password)
                        .addOnSuccessListener(new OnSuccessListener<AuthResult>() {
                            @Override
                            public void onSuccess(AuthResult authResult) {
                                Toast.makeText(MainActivity.this, "Signed In", Toast.LENGTH_SHORT).show();
                                Log.d("DONE","Logged in successfully!");
                                startActivity(new Intent(MainActivity.this,HomeActivity.class));
                                finish();
                            }
                        })
                        .addOnFailureListener(new OnFailureListener() {
                            @Override
                            public void onFailure(@NonNull Exception e) {
                                Toast.makeText(MainActivity.this, "try again later", Toast.LENGTH_SHORT).show();
                            }
                        });
            }

        });


    }
}