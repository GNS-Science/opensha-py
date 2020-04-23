package org.opensha.py;

import java.awt.geom.Point2D;
import java.util.LinkedList;
import java.util.List;

/**
	result container 
**/
public class HazardCalculatorResult {

	public List<String> infoList = new LinkedList<String>();
	public List<String> siteParamList = new LinkedList<String>();
	public List<Point2D> pgaCurveList = new LinkedList<Point2D>();
	public List<Point2D> saCurveList = new LinkedList<Point2D>();

	public List<String> info() {
		return this.infoList;
	}

	public List<String> siteParameters() {
		return this.siteParamList;
	}

	public List<Point2D> pgaCurve() {
		return this.pgaCurveList;
	}

	public List<Point2D> saCurve() {
		return this.saCurveList;
	}

	public static void main(String[] args) {};	
}
