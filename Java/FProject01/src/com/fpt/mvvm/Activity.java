package com.fpt.mvvm;

public abstract class Activity<VM extends ViewModel<?>> {
	protected VM viewModel;
	
	public Activity() {
		viewModel = createViewModel();
		onCreateView();
	}

	protected abstract VM createViewModel();
	
	public void start() {
		
	}
	
	abstract void onCreateView();
	
	public void finish() {
		
	}
	
}
