package com.macht.amanda;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.widget.CompoundButton;
import android.widget.Switch;

import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseError;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import com.google.firebase.database.ValueEventListener;

public class HomeActivity extends AppCompatActivity {

    Switch Port1, Port2, Port3 ,Port4 ,Port5, Port6;
    FirebaseAuth firebaseAuth;
    DatabaseReference databaseReference,p1,p2,p3,p4,p5,p6;
    String s1,s2,s3,s4,s5,s6;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_home);

        databaseReference = FirebaseDatabase.getInstance().getReference();
        Port1 = findViewById(R.id.port1Switch);
        Port2 = findViewById(R.id.port2switch);
        Port3 = findViewById(R.id.port3Switch);
        Port4 = findViewById(R.id.port4Switch);
        Port5 = findViewById(R.id.port5Switch);
        Port6 = findViewById(R.id.port6Switch);
        p1 = databaseReference.child("D1");
        p2 = databaseReference.child("D2");
        p3 = databaseReference.child("D3");
        p4 = databaseReference.child("D4");
        p5 = databaseReference.child("D5");
        p6 = databaseReference.child("D6");

        p1.addValueEventListener(new ValueEventListener() {
            @Override
            public void onDataChange(@NonNull DataSnapshot snapshot) {
                s1 = snapshot.getValue(String.class);
                if(s1.equals("ON")){
                    Port1.setChecked(true);
                }else{
                    Port1.setChecked(false);
                }
            }
            @Override
            public void onCancelled(@NonNull DatabaseError error) {

            }
        });

        p2.addValueEventListener(new ValueEventListener() {
            @Override
            public void onDataChange(@NonNull DataSnapshot snapshot) {
                s2 = snapshot.getValue(String.class);
                if(s2.equals("ON")){
                    Port2.setChecked(true);
                }else{
                    Port2.setChecked(false);
                }
            }

            @Override
            public void onCancelled(@NonNull DatabaseError error) {

            }
        });


        Port1.setOnCheckedChangeListener(new CompoundButton.OnCheckedChangeListener() {
            @Override
            public void onCheckedChanged(CompoundButton buttonView, boolean isChecked) {
                if (Port1.isChecked()){
                    databaseReference.child("D1").setValue("ON");
                }else{
                    databaseReference.child("D1").setValue("OFF");
                }
            }
        });

        Port2.setOnCheckedChangeListener((buttonView, isChecked) -> {
            if (Port2.isChecked()){
                databaseReference.child("D2").setValue("ON");
            }else{
                databaseReference.child("D2").setValue("OFF");
            }
        });

        Port3.setOnCheckedChangeListener(new CompoundButton.OnCheckedChangeListener() {
            @Override
            public void onCheckedChanged(CompoundButton buttonView, boolean isChecked) {
                if (Port3.isChecked()){
                    databaseReference.child("D3").setValue("ON");
                }else{
                    databaseReference.child("D3").setValue("OFF");
                }
            }
        });

        Port4.setOnCheckedChangeListener(new CompoundButton.OnCheckedChangeListener() {
            @Override
            public void onCheckedChanged(CompoundButton buttonView, boolean isChecked) {
                if (Port4.isChecked()){
                    databaseReference.child("D4").setValue("ON");
                }else{
                    databaseReference.child("D4").setValue("OFF");
                }
            }
        });

        Port5.setOnCheckedChangeListener(new CompoundButton.OnCheckedChangeListener() {
            @Override
            public void onCheckedChanged(CompoundButton buttonView, boolean isChecked) {
                if (Port5.isChecked()){
                    databaseReference.child("D5").setValue("ON");
                }else{
                    databaseReference.child("D5").setValue("OFF");
                }
            }
        });

        Port6.setOnCheckedChangeListener(new CompoundButton.OnCheckedChangeListener() {
            @Override
            public void onCheckedChanged(CompoundButton buttonView, boolean isChecked) {
                if (Port6.isChecked()){
                    databaseReference.child("D6").setValue("ON");
                }else{
                    databaseReference.child("D6").setValue("OFF");
                }
            }
        });



    }
}