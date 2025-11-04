package com.fpt.db;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Scanner;
import java.util.StringTokenizer;

import com.fpt.Config;

public interface IShareReference {
	
	public static IShareReference create(String dbName) {
		return new ShareReference(dbName);
	}
	
	public static IShareReference create() {
		return new ShareReference(IShareReference.class.getName());
	}
	
	void  setValue(String key, Object value);
	
	<T> T getValue(String key, T defaultValue);
	
	String getValueString(String key, String defaultValue);
}


class ShareReference implements IShareReference{
	private static final String TAG = "ShareReference";
	private String dbName;
	public ShareReference(String dbName) {
		this.dbName = dbName;
		
		File file = Config.getFile(dbName);
		try {
			if(!file.exists()) {
				file.createNewFile();
			}
		} catch (IOException e) {
			e.printStackTrace();
		}
		Log.d(TAG, file.getAbsolutePath() + " " + file.exists());
	}

	private ArrayList<Data> getDataList(){
		ArrayList<Data> results = new ArrayList<Data>();
        Scanner scanner = null;
		try {
			scanner = new Scanner(Config.getFile(dbName));
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		}
        while (scanner!= null && scanner.hasNextLine()) {
            String line = scanner.nextLine();
            Data data = new Data(line);
            if(data.hasKey()) {
            	results.add(new Data(line));
            }
        }
        
        if(scanner!= null) {
        	scanner.close();
        }
		return results;
	}
	
	@Override
	public void setValue(String key, Object value) {
		ArrayList<Data> results = getDataList();
		boolean updated = false;
		for(int i =0; i < results.size(); i ++) {
			Data result = results.get(i);
			if(key.equals(result.getKey())) {
				result.setValue(value == null ? "" : value.toString());
				updated = true;
			}
		}
		if(!updated) {
			results.add(new Data(key, value == null ? "" : value.toString()));
		}
		
		try (FileWriter writer = new FileWriter(Config.getFile(dbName).getAbsolutePath())) {
			for(int i =0; i < results.size(); i ++) {
				 writer.write(results.get(i).getData());
				 writer.write("\n");
			}
        } catch (IOException e) {
            e.printStackTrace();
        }
	}

	@SuppressWarnings("unchecked")
	@Override
	public <T> T getValue(String key, T defaultValue) {
		String currentValue = getValueString(key, defaultValue != null ? defaultValue.toString() : "");
		try {
			if(defaultValue instanceof Boolean) {
				return (T)((Object)Boolean.parseBoolean(currentValue));
			}else if(defaultValue instanceof Long) {
				return (T)((Object)Long.parseLong(currentValue));	
			}else if(defaultValue instanceof Integer) {	
				return (T)((Object)Integer.parseInt(currentValue));
			}else if(defaultValue instanceof Double) {
				return (T)((Object)Double.parseDouble(currentValue));
			}else if(defaultValue instanceof Float) {
				return (T)((Object)Float.parseFloat(currentValue));
			}else if(defaultValue instanceof String) {
				return (T)currentValue;
			}
		}catch (Exception e) {
			// do nothing
		}
		return defaultValue;	
	}

	@Override
	public String getValueString(String key, String defaultValue) {
		String result = defaultValue;
		ArrayList<Data> results = getDataList();
		for(Data data : results) {
			if(key.equals(data.getKey())) {
				result = data.getValue();
			}
		}
		return result != null ? result : defaultValue;
	}
}


class Log {
	public static void d(String tag, String message) {
		System.out.println(tag + ": " + message);
	}
}

class Data{
	private static final String TOKEN = "#@";
	private String key;
	private String value;
	public String getKey() {
		return key;
	}
	public String getData() {
		
		return key + TOKEN + (value == null ? "" : value);
	}
	public void setKey(String key) {
		this.key = key;
	}
	public String getValue() {
		return value;
	}
	public void setValue(String value) {
		this.value = value;
	}
	public Data(String key, String value) {
		super();
		this.key = key;
		this.value = value;
	}
	public Data(String line) {
		StringTokenizer tokenizer = new StringTokenizer(line, TOKEN);
		
		if(tokenizer.hasMoreTokens()) {
			key = tokenizer.nextToken();
		}
		
		if(tokenizer.hasMoreTokens()) {
			value = tokenizer.nextToken();
		}
		
	}
	public boolean hasKey() {
		return key != null && !key.trim().isBlank();
	}
}
