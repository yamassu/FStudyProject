package com.fpt;

import java.io.File;

public class Config {
	public static final String SAVE_FOLDER = "C:\\FProject01";
	public static final void createSaveFolder() {
		new File(SAVE_FOLDER).mkdirs();
	}
	
	public static File getFile(String name) {
		return new File(SAVE_FOLDER, name);
	}
}
