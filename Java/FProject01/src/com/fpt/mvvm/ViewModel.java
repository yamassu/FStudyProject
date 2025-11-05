package com.fpt.mvvm;

public abstract class ViewModel<Repo extends Repository> {
	protected Repo repository;
	
	public ViewModel(Repo repo) {
		this.repository = repo;
	}

}
