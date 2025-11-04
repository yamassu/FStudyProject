package com.fpt;

import com.fpt.db.IShareReference;

public class Main {
	public static void main(String[] args) {
		System.out.println("ABC");
		Config.createSaveFolder();
		
		IShareReference shareReference = IShareReference.create();
		String key = "test";
		System.out.println(shareReference.getValueString(key, ""));
		shareReference.setValue(key, "1111");
		System.out.println(shareReference.getValueString(key, ""));
	}
}
