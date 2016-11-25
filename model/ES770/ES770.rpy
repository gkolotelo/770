I-Logix-RPY-Archive version 8.5.2 Modeler C++ 1159120
{ IProject 
	- _id = GUID 25bca5c2-3f14-482b-97d9-efb6fc58d91f;
	- _myState = 8192;
	- _name = "ES770";
	- _objectCreation = "59175112546201610308631159";
	- _umlDependencyID = "2005";
	- _lastID = 24;
	- _UserColors = { IRPYRawContainer 
		- size = 16;
		- value = 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 
	}
	- _defaultSubsystem = { ISubsystemHandle 
		- _m2Class = "ISubsystem";
		- _filename = "Sources.sbs";
		- _subsystem = "";
		- _class = "";
		- _name = "Sources";
		- _id = GUID f9623802-9e64-4088-b484-572be495c316;
	}
	- _component = { IHandle 
		- _m2Class = "IComponent";
		- _filename = "FRDM_KL25Z.cmp";
		- _subsystem = "";
		- _class = "";
		- _name = "FRDM_KL25Z";
		- _id = GUID e14c6d7e-2527-4591-8d47-f61912c80b65;
	}
	- Multiplicities = { IRPYRawContainer 
		- size = 4;
		- value = 
		{ IMultiplicityItem 
			- _name = "1";
			- _count = -1;
		}
		{ IMultiplicityItem 
			- _name = "*";
			- _count = -1;
		}
		{ IMultiplicityItem 
			- _name = "0,1";
			- _count = -1;
		}
		{ IMultiplicityItem 
			- _name = "1..*";
			- _count = -1;
		}
	}
	- Subsystems = { IRPYRawContainer 
		- size = 4;
		- value = 
		{ ISubsystem 
			- fileName = "Sources";
			- _id = GUID f9623802-9e64-4088-b484-572be495c316;
		}
		{ ISubsystem 
			- fileName = "Requirements";
			- _id = GUID 24b2c2cb-2b3a-42ab-976e-1909af601173;
		}
		{ ISubsystem 
			- fileName = "System";
			- _id = GUID 07685dbe-5566-4a67-8dda-a128e6d2b138;
		}
		{ ISubsystem 
			- fileName = "package_23";
			- _id = GUID 417f0741-af53-4cf8-8db4-14d8a7e3fcd2;
		}
	}
	- Diagrams = { IRPYRawContainer 
		- size = 4;
		- value = 
		{ IDiagram 
			- _id = GUID bc5b3b92-b5fc-4a8d-8558-b5ba0e29f33f;
			- _myState = 8192;
			- _properties = { IPropertyContainer 
				- Subjects = { IRPYRawContainer 
					- size = 2;
					- value = 
					{ IPropertySubject 
						- _Name = "Format";
						- Metaclasses = { IRPYRawContainer 
							- size = 5;
							- value = 
							{ IPropertyMetaclass 
								- _Name = "Actor";
								- Properties = { IRPYRawContainer 
									- size = 7;
									- value = 
									{ IProperty 
										- _Name = "DefaultSize";
										- _Value = "0,26,84,168";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Fill.FillColor";
										- _Value = "255,255,255";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,128";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "111,0,107";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "Comment";
								- Properties = { IRPYRawContainer 
									- size = 7;
									- value = 
									{ IProperty 
										- _Name = "DefaultSize";
										- _Value = "0,0,84,96";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Fill.FillColor";
										- _Value = "255,255,207";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "225,225,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "Component";
								- Properties = { IRPYRawContainer 
									- size = 7;
									- value = 
									{ IProperty 
										- _Name = "DefaultSize";
										- _Value = "0,0,276,180";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Fill.FillColor";
										- _Value = "255,255,255";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "0,16,230";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "Flow";
								- Properties = { IRPYRawContainer 
									- size = 6;
									- value = 
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,128";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "0,112,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineStyle";
										- _Value = "1";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "0";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "Note";
								- Properties = { IRPYRawContainer 
									- size = 7;
									- value = 
									{ IProperty 
										- _Name = "DefaultSize";
										- _Value = "0,0,84,96";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Fill.FillColor";
										- _Value = "255,255,207";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "225,225,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
						}
					}
					{ IPropertySubject 
						- _Name = "General";
						- Metaclasses = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertyMetaclass 
								- _Name = "Graphics";
								- Properties = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IProperty 
										- _Name = "grid_snap";
										- _Value = "True";
										- _Type = Bool;
									}
								}
							}
						}
					}
				}
			}
			- _name = "overview";
			- _objectCreation = "59175132546201610308611159";
			- _umlDependencyID = "2582";
			- _lastModifiedTime = "9.14.2016::2:24:25";
			- _graphicChart = { CGIClassChart 
				- _id = GUID 5e9ecb70-0443-4ff1-8317-73ce5b577cae;
				- m_type = 0;
				- m_pModelObject = { IHandle 
					- _m2Class = "IDiagram";
					- _id = GUID bc5b3b92-b5fc-4a8d-8558-b5ba0e29f33f;
				}
				- m_pParent = ;
				- m_name = { CGIText 
					- m_str = "";
					- m_style = "Arial" 10 0 0 0 1 ;
					- m_color = { IColor 
						- m_fgColor = 0;
						- m_bgColor = 0;
						- m_bgFlag = 0;
					}
					- m_position = 1 0 0  ;
					- m_nIdent = 0;
					- m_bImplicitSetRectPoints = 0;
					- m_nOrientationCtrlPt = 8;
				}
				- m_drawBehavior = 0;
				- m_bIsPreferencesInitialized = 0;
				- elementList = 35;
				{ CGIClass 
					- _id = GUID 80730c39-2911-414c-8de5-60d13e2002eb;
					- m_type = 78;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "Sources.sbs";
						- _subsystem = "Sources";
						- _class = "";
						- _name = "TopLevel";
						- _id = GUID c96d5194-58ed-4182-82e6-04845c227d30;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "TopLevel";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 0;
					- m_bIsPreferencesInitialized = 0;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 0 ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Attrs = { IRPYRawContainer 
						- size = 0;
					}
					- Operations = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIComponent 
					- _id = GUID 305e7180-bf23-43d5-92d6-18ff4b598fd5;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 145;
					- m_pModelObject = { IHandle 
						- _m2Class = "IComponent";
						- _filename = "FRDM_KL25Z.cmp";
						- _subsystem = "";
						- _class = "";
						- _name = "FRDM_KL25Z";
						- _id = GUID e14c6d7e-2527-4591-8d47-f61912c80b65;
					}
					- m_pParent = GUID 80730c39-2911-414c-8de5-60d13e2002eb;
					- m_name = { CGIText 
						- m_str = "FRDM_KL25Z";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 4104;
					- m_transform = 0.284265 0 0 0.167626 623.715 131.832 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 1 1  1 1218  1183 1218  1183 1  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				{ CGIComponent 
					- _id = GUID 2c44de4a-0423-42aa-9310-62b4a41b8dc0;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 145;
					- m_pModelObject = { IHandle 
						- _m2Class = "IComponent";
						- _filename = "ADC0.cmp";
						- _subsystem = "";
						- _class = "";
						- _name = "FRDM_KL25Z\\ADC0";
						- _id = GUID 4465b3a3-1d75-4c0b-a65e-e10ac6fa3543;
					}
					- m_pParent = GUID 305e7180-bf23-43d5-92d6-18ff4b598fd5;
					- m_name = { CGIText 
						- m_str = "ADC0";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 4104;
					- m_transform = 0.287094 0 0 0.294686 802.7 789.78 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 1 1  1 1218  1183 1218  1183 1  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				{ CGIComponent 
					- _id = GUID 3a07ea13-c009-4301-8453-9ead1eef06f1;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 145;
					- m_pModelObject = { IHandle 
						- _m2Class = "IComponent";
						- _filename = "Battery.cmp";
						- _subsystem = "";
						- _class = "";
						- _name = "Regulator_5V\\Battery";
						- _id = GUID 79b61cec-acf8-4488-909b-1988c728e3a0;
					}
					- m_pParent = GUID 80730c39-2911-414c-8de5-60d13e2002eb;
					- m_name = { CGIText 
						- m_str = "Battery";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 4104;
					- m_transform = 0.133476 0 0 0.0807607 84.168 131.475 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 1 1  1 1218  1183 1218  1183 1  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				{ CGIComponent 
					- _id = GUID 8c264ffe-3b7b-4166-9774-453259715c57;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 145;
					- m_pModelObject = { IHandle 
						- _m2Class = "IComponent";
						- _filename = "Driver.cmp";
						- _subsystem = "";
						- _class = "";
						- _name = "Driver";
						- _id = GUID e8d2b136-7b20-43f7-91cd-12cd608855ae;
					}
					- m_pParent = GUID 80730c39-2911-414c-8de5-60d13e2002eb;
					- m_name = { CGIText 
						- m_str = "Driver";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 4104;
					- m_transform = 0.133476 0 0 0.0807607 323.448 325.221 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 1 1  1 1218  1183 1218  1183 1  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				{ CGIComponent 
					- _id = GUID 4ad300eb-b1fb-40e1-aa07-95edfe4a49a7;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 145;
					- m_pModelObject = { IHandle 
						- _m2Class = "IComponent";
						- _filename = "Encoder_A.cmp";
						- _subsystem = "";
						- _class = "";
						- _name = "Encoder_A";
						- _id = GUID ce24be95-baea-4ba5-9cd9-9124f23a155b;
					}
					- m_pParent = GUID 80730c39-2911-414c-8de5-60d13e2002eb;
					- m_name = { CGIText 
						- m_str = "Encoder_A";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 4104;
					- m_transform = 0.133476 0 0 0.0807607 767.61 479.824 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 1 1  1 1218  1183 1218  1183 1  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				{ CGIComponent 
					- _id = GUID d603146e-bc24-48a3-858b-e12d2e5b4b03;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 145;
					- m_pModelObject = { IHandle 
						- _m2Class = "IComponent";
						- _filename = "Encoder_B.cmp";
						- _subsystem = "";
						- _class = "";
						- _name = "Encoder_B";
						- _id = GUID 199a0090-41bd-4581-ac47-f1c6366635f8;
					}
					- m_pParent = GUID 80730c39-2911-414c-8de5-60d13e2002eb;
					- m_name = { CGIText 
						- m_str = "Encoder_B";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 4104;
					- m_transform = 0.133476 0 0 0.0807607 600.192 480.126 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 1 1  1 1218  1183 1218  1183 1  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				{ CGIComponent 
					- _id = GUID 0cbf5c16-943e-4648-92d5-0c3d1d5f2917;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 145;
					- m_pModelObject = { IHandle 
						- _m2Class = "IComponent";
						- _filename = "IR_Array.cmp";
						- _subsystem = "";
						- _class = "";
						- _name = "IR_Array";
						- _id = GUID 9d7eef10-fb9b-4f5d-ad99-d6368ca646c1;
					}
					- m_pParent = GUID 80730c39-2911-414c-8de5-60d13e2002eb;
					- m_name = { CGIText 
						- m_str = "IR_Array";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 4104;
					- m_transform = 0.133476 0 0 0.0807607 971.773 479.427 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 1 1  1 1218  1183 1218  1183 1  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				{ CGIComponent 
					- _id = GUID e5101584-c606-4f44-a75a-785614304b26;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 145;
					- m_pModelObject = { IHandle 
						- _m2Class = "IComponent";
						- _filename = "Motor_A.cmp";
						- _subsystem = "";
						- _class = "";
						- _name = "Motor_A";
						- _id = GUID 07dce727-5e4f-4cff-aa6c-39dfbb3e9658;
					}
					- m_pParent = GUID 80730c39-2911-414c-8de5-60d13e2002eb;
					- m_name = { CGIText 
						- m_str = "Motor_A";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 4104;
					- m_transform = 0.133476 0 0 0.0807607 227.935 480.03 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 1 1  1 1218  1183 1218  1183 1  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				{ CGIComponent 
					- _id = GUID b64890de-54f7-4760-afbc-a600d8e51e9a;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 145;
					- m_pModelObject = { IHandle 
						- _m2Class = "IComponent";
						- _filename = "Motor_B.cmp";
						- _subsystem = "";
						- _class = "";
						- _name = "Motor_B";
						- _id = GUID 5c9146fc-4bd2-422a-a71f-3f13a2125b14;
					}
					- m_pParent = GUID 80730c39-2911-414c-8de5-60d13e2002eb;
					- m_name = { CGIText 
						- m_str = "Motor_B";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 4104;
					- m_transform = 0.133476 0 0 0.0807607 395.517 480.332 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 1 1  1 1218  1183 1218  1183 1  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				{ CGIComponent 
					- _id = GUID d851b84c-d869-4f32-a9fa-f294b84a3058;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 145;
					- m_pModelObject = { IHandle 
						- _m2Class = "IComponent";
						- _filename = "Regulator_5V.cmp";
						- _subsystem = "";
						- _class = "";
						- _name = "Regulator_5V";
						- _id = GUID ab85102d-b980-4ba3-a86d-c3bffa018e58;
					}
					- m_pParent = GUID 80730c39-2911-414c-8de5-60d13e2002eb;
					- m_name = { CGIText 
						- m_str = "Regulator_5V";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 4104;
					- m_transform = 0.13198 0 0 0.0788827 359.868 131.921 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 1 1  1 1218  1183 1218  1183 1  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				{ CGIComponent 
					- _id = GUID 409f593e-3288-4a8b-9339-2ff3177aa5fd;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 145;
					- m_pModelObject = { IHandle 
						- _m2Class = "IComponent";
						- _filename = "TPM0.cmp";
						- _subsystem = "";
						- _class = "";
						- _name = "FRDM_KL25Z\\TPM0";
						- _id = GUID db757bae-42ea-4511-acde-185bb3a3ba35;
					}
					- m_pParent = GUID 305e7180-bf23-43d5-92d6-18ff4b598fd5;
					- m_name = { CGIText 
						- m_str = "TPM0";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 4104;
					- m_transform = 0.291925 0 0 0.284313 40.6094 358.792 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 1 1  1 1218  1183 1218  1183 1  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				{ CGIBasicClass 
					- _id = GUID 245a59cd-f02e-4603-b57f-22eee3209dc3;
					- m_type = 124;
					- m_pModelObject = { IHandle 
						- _m2Class = "IActor";
						- _filename = "System.sbs";
						- _subsystem = "System";
						- _class = "";
						- _name = "User";
						- _id = GUID f5ec02a4-e90a-481c-ab43-646c84e34c5a;
					}
					- m_pParent = GUID 80730c39-2911-414c-8de5-60d13e2002eb;
					- m_name = { CGIText 
						- m_str = "System::User";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.077634 0 0 0.123909 1081.89 77.0227 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 40 250  40 1396  1122 1396  1122 250  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				{ CGIInformationFlow 
					- _id = GUID 2e23a513-91fc-4cb1-ad3b-842988bc0fc4;
					- m_type = 180;
					- m_pModelObject = { IHandle 
						- _m2Class = "IInformationFlow";
						- _filename = "System.sbs";
						- _subsystem = "System";
						- _class = "";
						- _name = "TPM0_Driver";
						- _id = GUID 726d80fd-195a-4ae4-b7f8-372c84a5223b;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 409f593e-3288-4a8b-9339-2ff3177aa5fd;
					- m_sourceType = 'F';
					- m_pTarget = GUID 8c264ffe-3b7b-4166-9774-453259715c57;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 1 398 239  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 138 983 ;
					- m_TargetPort = 559 -15 ;
					- m_bShowKeyword = 1;
					- m_showConveyed = name;
					- m_keyword = { CGIText 
						- m_str = "\쳀low\�";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  48 -9  48 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 438 285 ;
						- m_nHorizontalSpacing = -32;
						- m_nVerticalSpacing = -8;
						- m_nOrientationCtrlPt = 8;
					}
					- m_conveyed = { CGIText 
						- m_str = "Control_Signals";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  109 -9  109 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 498 285 ;
						- m_nHorizontalSpacing = 1;
						- m_nVerticalSpacing = 27;
						- m_nOrientationCtrlPt = 7;
					}
					- m_direction = type_122;
				}
				{ CGIAnnotation 
					- _id = GUID 015da14d-45ad-4346-8442-e008e95a08b0;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 173;
					- m_pModelObject = { IHandle 
						- _m2Class = "IComment";
						- _filename = "System.sbs";
						- _subsystem = "System";
						- _class = "";
						- _name = "comment_13";
						- _id = GUID 69845d3b-596e-41ae-9ce0-d4f56ed325e9;
					}
					- m_pParent = GUID 80730c39-2911-414c-8de5-60d13e2002eb;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.132841 0 0 0.120879 168 311.637 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 0 3  0 1095  1084 1095  1084 3  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- _iTempdisplayTextFlag = 2;
					- m_bIsBoxStyle = 0;
				}
				{ CGIInformationFlow 
					- _id = GUID 4dacf3a6-13d8-4346-a421-0b372bb9983a;
					- m_type = 180;
					- m_pModelObject = { IHandle 
						- _m2Class = "IInformationFlow";
						- _filename = "System.sbs";
						- _subsystem = "System";
						- _class = "";
						- _name = "Driver_Motor_A";
						- _id = GUID d107a65f-6a2e-44c2-a342-9c7e11b78a46;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 8c264ffe-3b7b-4166-9774-453259715c57;
					- m_sourceType = 'F';
					- m_pTarget = GUID e5101584-c606-4f44-a75a-785614304b26;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 2 360 451  308 451  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 274 1174 ;
					- m_TargetPort = 600 -13 ;
					- m_bShowKeyword = 1;
					- m_showConveyed = name;
					- m_keyword = { CGIText 
						- m_str = "\쳀low\�";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  48 -9  48 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 426 393 ;
						- m_nHorizontalSpacing = 6;
						- m_nVerticalSpacing = -6;
						- m_nOrientationCtrlPt = 8;
					}
					- m_conveyed = { CGIText 
						- m_str = "PWM_A";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -30 -8  34 -8  34 10  -30 10  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 378 392 ;
						- m_nHorizontalSpacing = -93;
						- m_nVerticalSpacing = 29;
						- m_nOrientationCtrlPt = 7;
					}
					- m_direction = type_122;
				}
				{ CGIInformationFlow 
					- _id = GUID b321e60a-943d-43bb-bff8-7bba68ff3791;
					- m_type = 180;
					- m_pModelObject = { IHandle 
						- _m2Class = "IInformationFlow";
						- _filename = "System.sbs";
						- _subsystem = "System";
						- _class = "";
						- _name = "Driver_Motor_B";
						- _id = GUID 50ae50c8-d236-4c90-9479-d28e1650788a;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 8c264ffe-3b7b-4166-9774-453259715c57;
					- m_sourceType = 'F';
					- m_pTarget = GUID b64890de-54f7-4760-afbc-a600d8e51e9a;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 2 432 451  475 451  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 813 1174 ;
					- m_TargetPort = 595 -16 ;
					- m_bShowKeyword = 1;
					- m_showConveyed = name;
					- m_keyword = { CGIText 
						- m_str = "\쳀low\�";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  48 -9  48 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 534 393 ;
						- m_nHorizontalSpacing = -7;
						- m_nVerticalSpacing = -6;
						- m_nOrientationCtrlPt = 8;
					}
					- m_conveyed = { CGIText 
						- m_str = "PWM_B";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -30 -8  34 -8  34 10  -30 10  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 618 392 ;
						- m_nHorizontalSpacing = 26;
						- m_nVerticalSpacing = 29;
						- m_nOrientationCtrlPt = 7;
					}
					- m_direction = type_122;
				}
				{ CGIInformationFlow 
					- _id = GUID 2eed0328-208e-497a-8275-4bb553cfe953;
					- m_type = 180;
					- m_pModelObject = { IHandle 
						- _m2Class = "IInformationFlow";
						- _filename = "System.sbs";
						- _subsystem = "System";
						- _class = "";
						- _name = "Motor_B_Encoder_B";
						- _id = GUID 38e11ce7-d72f-49d8-9e2c-bac02f76645c;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID b64890de-54f7-4760-afbc-a600d8e51e9a;
					- m_sourceType = 'F';
					- m_pTarget = GUID d603146e-bc24-48a3-858b-e12d2e5b4b03;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 2 468 614  678 614  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 543 1185 ;
					- m_TargetPort = 583 1212 ;
					- m_bShowKeyword = 1;
					- m_showConveyed = name;
					- m_keyword = { CGIText 
						- m_str = "\쳀low\�";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  48 -9  48 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 690 513 ;
						- m_nHorizontalSpacing = 30;
						- m_nVerticalSpacing = -36;
						- m_nOrientationCtrlPt = 8;
					}
					- m_conveyed = { CGIText 
						- m_str = "Wheel_B";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -29 -8  35 -8  35 10  -29 10  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 641 512 ;
						- m_nHorizontalSpacing = -69;
						- m_nVerticalSpacing = -1;
						- m_nOrientationCtrlPt = 7;
					}
					- m_direction = type_122;
				}
				{ CGIInformationFlow 
					- _id = GUID e08a30a7-8e4f-44e2-87ef-05667b235f64;
					- m_type = 180;
					- m_pModelObject = { IHandle 
						- _m2Class = "IInformationFlow";
						- _filename = "System.sbs";
						- _subsystem = "System";
						- _class = "";
						- _name = "Motor_A_Encoder_A";
						- _id = GUID f7059783-b90e-42f8-8f17-5e5a5b79be6c;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID e5101584-c606-4f44-a75a-785614304b26;
					- m_sourceType = 'F';
					- m_pTarget = GUID 4ad300eb-b1fb-40e1-aa07-95edfe4a49a7;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 2 300 628  840 628  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 540 1188 ;
					- m_TargetPort = 542 1216 ;
					- m_bShowKeyword = 1;
					- m_showConveyed = name;
					- m_keyword = { CGIText 
						- m_str = "\쳀low\�";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  48 -9  48 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 690 573 ;
						- m_nHorizontalSpacing = 33;
						- m_nVerticalSpacing = -3;
						- m_nOrientationCtrlPt = 8;
					}
					- m_conveyed = { CGIText 
						- m_str = "Wheel_A";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -29 -8  35 -8  35 10  -29 10  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 641 572 ;
						- m_nHorizontalSpacing = -66;
						- m_nVerticalSpacing = 32;
						- m_nOrientationCtrlPt = 7;
					}
					- m_direction = type_122;
				}
				{ CGIInformationFlow 
					- _id = GUID 2d87f359-ba70-49c7-8a75-3abfb9e84f4c;
					- m_type = 180;
					- m_pModelObject = { IHandle 
						- _m2Class = "IInformationFlow";
						- _filename = "Sources.sbs";
						- _subsystem = "Sources";
						- _class = "";
						- _name = "Encoder_A_TPM1";
						- _id = GUID 993b6810-d0ba-412c-933c-50b9aa9704ef;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 4ad300eb-b1fb-40e1-aa07-95edfe4a49a7;
					- m_sourceType = 'F';
					- m_pTarget = GUID 449ce760-4cc8-4035-a1eb-2134c6ad3b38;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 2 840 397  792 397  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 542 2 ;
					- m_TargetPort = 592 985 ;
					- m_bShowKeyword = 1;
					- m_showConveyed = name;
					- m_keyword = { CGIText 
						- m_str = "\쳀low\�";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  48 -9  48 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 966 357 ;
						- m_nHorizontalSpacing = 59;
						- m_nVerticalSpacing = 27;
						- m_nOrientationCtrlPt = 8;
					}
					- m_conveyed = { CGIText 
						- m_str = "CHA";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 7;
					}
					- m_direction = type_122;
				}
				{ CGIInformationFlow 
					- _id = GUID f901e18c-8a85-4a88-a519-151994d4ef3d;
					- m_type = 180;
					- m_pModelObject = { IHandle 
						- _m2Class = "IInformationFlow";
						- _filename = "Sources.sbs";
						- _subsystem = "Sources";
						- _class = "";
						- _name = "Encoder_B_TPM2";
						- _id = GUID 764a8fe5-828c-4bad-80dd-d53662c3abf2;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID d603146e-bc24-48a3-858b-e12d2e5b4b03;
					- m_sourceType = 'F';
					- m_pTarget = GUID a5aa6123-5a36-4248-bc9c-725331a6adcb;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 538 -2 ;
					- m_TargetPort = 439 984 ;
					- m_bShowKeyword = 1;
					- m_showConveyed = name;
					- m_keyword = { CGIText 
						- m_str = "\쳀low\�";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  48 -9  48 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 846 345 ;
						- m_nHorizontalSpacing = 18;
						- m_nVerticalSpacing = -5;
						- m_nOrientationCtrlPt = 8;
					}
					- m_conveyed = { CGIText 
						- m_str = "CHB";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -27 -8  32 -8  32 10  -27 10  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 819 344 ;
						- m_nHorizontalSpacing = -57;
						- m_nVerticalSpacing = 30;
						- m_nOrientationCtrlPt = 7;
					}
					- m_direction = type_122;
				}
				{ CGIInformationFlow 
					- _id = GUID db303470-f3a2-4a6a-adf2-181686116794;
					- m_type = 180;
					- m_pModelObject = { IHandle 
						- _m2Class = "IInformationFlow";
						- _filename = "System.sbs";
						- _subsystem = "System";
						- _class = "";
						- _name = "IR_Array_ADC0";
						- _id = GUID 6a20c765-4264-4104-9bca-8642da197c08;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 0cbf5c16-943e-4648-92d5-0c3d1d5f2917;
					- m_sourceType = 'F';
					- m_pTarget = GUID 2c44de4a-0423-42aa-9310-62b4a41b8dc0;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 1 1005 299  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 249 156 ;
					- m_TargetPort = 1141 704 ;
					- m_bShowKeyword = 1;
					- m_showConveyed = name;
					- m_keyword = { CGIText 
						- m_str = "\쳀low\�";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  48 -9  48 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 954 393 ;
						- m_nHorizontalSpacing = -10;
						- m_nVerticalSpacing = 32;
						- m_nOrientationCtrlPt = 8;
					}
					- m_conveyed = { CGIText 
						- m_str = "ADC_IR";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  57 -9  57 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 954 417 ;
						- m_nHorizontalSpacing = -72;
						- m_nVerticalSpacing = 56;
						- m_nOrientationCtrlPt = 7;
					}
					- m_direction = type_122;
				}
				{ CGIAnnotation 
					- _id = GUID 2a872625-5d00-4ab0-9288-bc41b48f44a5;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 173;
					- m_pModelObject = { IHandle 
						- _m2Class = "IComment";
						- _filename = "System.sbs";
						- _subsystem = "System";
						- _class = "";
						- _name = "comment_21";
						- _id = GUID 62a6d1f1-36db-41da-bc6e-7a4c6d02ef24;
					}
					- m_pParent = GUID 80730c39-2911-414c-8de5-60d13e2002eb;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.199262 0 0 0.0549451 960 587.835 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 0 3  0 1095  1084 1095  1084 3  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- _iTempdisplayTextFlag = 2;
					- m_bIsBoxStyle = 0;
				}
				{ CGIComponent 
					- _id = GUID b2129d85-b113-4edf-b1bb-797761ca79c3;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 145;
					- m_pModelObject = { IHandle 
						- _m2Class = "IComponent";
						- _filename = "GPIO.cmp";
						- _subsystem = "";
						- _class = "";
						- _name = "FRDM_KL25Z\\GPIO";
						- _id = GUID 6f402d72-a740-4a03-8db1-c017b46e9a16;
					}
					- m_pParent = GUID 305e7180-bf23-43d5-92d6-18ff4b598fd5;
					- m_name = { CGIText 
						- m_str = "GPIO";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 4104;
					- m_transform = 0.28882 0 0 0.306172 800.39 354.719 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 1 1  1 1218  1183 1218  1183 1  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				{ CGIInformationFlow 
					- _id = GUID f63a94c9-53bc-4632-9be3-a856c27d3beb;
					- m_type = 180;
					- m_pModelObject = { IHandle 
						- _m2Class = "IInformationFlow";
						- _filename = "System.sbs";
						- _subsystem = "System";
						- _class = "";
						- _name = "Regulator_5V_FRDM_KL25Z";
						- _id = GUID e32b8392-7add-4415-b1d7-773358c3279a;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID d851b84c-d869-4f32-a9fa-f294b84a3058;
					- m_sourceType = 'F';
					- m_pTarget = GUID 305e7180-bf23-43d5-92d6-18ff4b598fd5;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 1175 926 ;
					- m_TargetPort = 15 425 ;
					- m_bShowKeyword = 1;
					- m_showConveyed = name;
					- m_keyword = { CGIText 
						- m_str = "\쳀low\�";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  48 -9  48 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 546 213 ;
						- m_nHorizontalSpacing = -3;
						- m_nVerticalSpacing = -10;
						- m_nOrientationCtrlPt = 8;
					}
					- m_conveyed = { CGIText 
						- m_str = "Power";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -24 -8  28 -8  28 10  -24 10  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 684 128 ;
						- m_nHorizontalSpacing = -18;
						- m_nVerticalSpacing = 2;
						- m_nOrientationCtrlPt = 7;
					}
					- m_direction = type_122;
				}
				{ CGIInformationFlow 
					- _id = GUID a4bd855f-16a6-4936-a953-28f58871c870;
					- m_type = 180;
					- m_pModelObject = { IHandle 
						- _m2Class = "IInformationFlow";
						- _filename = "System.sbs";
						- _subsystem = "System";
						- _class = "";
						- _name = "Battery_Regulator_5V";
						- _id = GUID 2b1c1ece-adbe-4b1f-89a7-3004276791f3;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 3a07ea13-c009-4301-8453-9ead1eef06f1;
					- m_sourceType = 'F';
					- m_pTarget = GUID d851b84c-d869-4f32-a9fa-f294b84a3058;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 1167 898 ;
					- m_TargetPort = 39 939 ;
					- m_bShowKeyword = 1;
					- m_showConveyed = name;
					- m_keyword = { CGIText 
						- m_str = "\쳀low\�";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_conveyed = { CGIText 
						- m_str = "Batt_Pwr";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -32 -8  37 -8  37 10  -32 10  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 416 116 ;
						- m_nHorizontalSpacing = -25;
						- m_nVerticalSpacing = -2;
						- m_nOrientationCtrlPt = 7;
					}
					- m_direction = type_122;
				}
				{ CGIInformationFlow 
					- _id = GUID 793525b4-aed2-47e6-a17f-3c4df193d9db;
					- m_type = 180;
					- m_pModelObject = { IHandle 
						- _m2Class = "IInformationFlow";
						- _filename = "System.sbs";
						- _subsystem = "System";
						- _class = "";
						- _name = "Battery_Driver";
						- _id = GUID fc400fd9-9ed2-49c1-9ea0-c3244046c3fd;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 3a07ea13-c009-4301-8453-9ead1eef06f1;
					- m_sourceType = 'F';
					- m_pTarget = GUID 8c264ffe-3b7b-4166-9774-453259715c57;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 2 168 301  372 301  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 628 1195 ;
					- m_TargetPort = 364 47 ;
					- m_bShowKeyword = 1;
					- m_showConveyed = name;
					- m_keyword = { CGIText 
						- m_str = "\쳀low\�";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  48 -9  48 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 330 201 ;
						- m_nHorizontalSpacing = -27;
						- m_nVerticalSpacing = -36;
						- m_nOrientationCtrlPt = 8;
					}
					- m_conveyed = { CGIText 
						- m_str = "Batt_Pwr";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 7;
					}
					- m_direction = type_122;
				}
				{ CGIInformationFlow 
					- _id = GUID 098a9c09-40e1-4504-bdc7-e9619614f7ef;
					- m_type = 180;
					- m_pModelObject = { IHandle 
						- _m2Class = "IInformationFlow";
						- _filename = "System.sbs";
						- _subsystem = "System";
						- _class = "";
						- _name = "User_GPIO";
						- _id = GUID 740b6e89-8166-425c-a467-e7a89b28ac2c;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 245a59cd-f02e-4603-b57f-22eee3209dc3;
					- m_sourceType = 'F';
					- m_pTarget = GUID b2129d85-b113-4edf-b1bb-797761ca79c3;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 2 977 180  977 230  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 439 831 ;
					- m_TargetPort = 1166 754 ;
					- m_bShowKeyword = 1;
					- m_showConveyed = name;
					- m_keyword = { CGIText 
						- m_str = "\쳀low\�";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_conveyed = { CGIText 
						- m_str = "Diag_SW";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -33 -8  39 -8  39 10  -33 10  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 1125 128 ;
						- m_nHorizontalSpacing = -8;
						- m_nVerticalSpacing = -4;
						- m_nOrientationCtrlPt = 7;
					}
					- m_direction = type_122;
				}
				{ CGIAnnotation 
					- _id = GUID 10413ef2-c677-41c8-b5f8-a597a230b655;
					- m_type = 173;
					- m_pModelObject = { IHandle 
						- _m2Class = "IComment";
						- _filename = "System.sbs";
						- _subsystem = "System";
						- _class = "";
						- _name = "comment_26";
						- _id = GUID 37c1a971-e435-4c9e-b610-bd8e72d13f5e;
					}
					- m_pParent = GUID 80730c39-2911-414c-8de5-60d13e2002eb;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.110701 0 0 0.0769231 1176 143.769 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 0 3  0 1095  1084 1095  1084 3  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- _iTempdisplayTextFlag = 2;
					- m_bIsBoxStyle = 0;
				}
				{ CGIAnnotation 
					- _id = GUID 3f97aff3-f7aa-464c-9959-ac7bcf2c31d8;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 173;
					- m_pModelObject = { IHandle 
						- _m2Class = "IComment";
						- _filename = "System.sbs";
						- _subsystem = "System";
						- _class = "";
						- _name = "comment_27";
						- _id = GUID e19a1aa0-bd23-4772-8bd0-9d3555619b23;
					}
					- m_pParent = GUID 80730c39-2911-414c-8de5-60d13e2002eb;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.221402 0 0 0.0549451 456 659.835 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 0 3  0 1095  1084 1095  1084 3  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- _iTempdisplayTextFlag = 2;
					- m_bIsBoxStyle = 0;
				}
				{ CGIAnnotation 
					- _id = GUID 5621b181-3aa9-407e-85db-b8109a8d3021;
					- m_type = 90;
					- m_pModelObject = { IHandle 
						- _m2Class = "";
					}
					- m_pParent = GUID 80730c39-2911-414c-8de5-60d13e2002eb;
					- m_name = { CGIText 
						- m_str = "ES770 - Digital Systems Lab.
2S2016

Overview of System";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 4096;
					- m_transform = 0.298893 0 0 0.0638686 36 11.8084 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 0 3  0 1099  1084 1099  1084 3  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- _iTempdisplayTextFlag = 1;
					- m_bIsBoxStyle = 0;
				}
				{ CGIComponent 
					- _id = GUID 449ce760-4cc8-4035-a1eb-2134c6ad3b38;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 145;
					- m_pModelObject = { IHandle 
						- _m2Class = "IComponent";
						- _filename = "TPM1.cmp";
						- _subsystem = "";
						- _class = "";
						- _name = "FRDM_KL25Z\\TPM1";
						- _id = GUID 6b5ea975-1085-46b7-92cb-bad6f350a40b;
					}
					- m_pParent = GUID 305e7180-bf23-43d5-92d6-18ff4b598fd5;
					- m_name = { CGIText 
						- m_str = "TPM1";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 4104;
					- m_transform = 0.286079 0 0 0.294116 422.641 785.121 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 1 1  1 1218  1183 1218  1183 1  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				{ CGIComponent 
					- _id = GUID a5aa6123-5a36-4248-bc9c-725331a6adcb;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 145;
					- m_pModelObject = { IHandle 
						- _m2Class = "IComponent";
						- _filename = "TPM2.cmp";
						- _subsystem = "";
						- _class = "";
						- _name = "FRDM_KL25Z\\TPM2";
						- _id = GUID e06d517f-73ae-4744-a1ed-e9ec23416f3a;
					}
					- m_pParent = GUID 305e7180-bf23-43d5-92d6-18ff4b598fd5;
					- m_name = { CGIText 
						- m_str = "TPM2";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 4104;
					- m_transform = 0.284324 0 0 0.294116 45.0251 785.455 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 1 1  1 1218  1183 1218  1183 1  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				{ CGIInformationFlow 
					- _id = GUID 0252d72e-e6fb-4d31-88de-78c201cbf5a3;
					- m_type = 180;
					- m_pModelObject = { IHandle 
						- _m2Class = "IInformationFlow";
						- _filename = "Sources.sbs";
						- _subsystem = "Sources";
						- _class = "";
						- _name = "GPIO_IR_Array";
						- _id = GUID 7032f65e-01a9-444a-b7e4-3fdee6916d98;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID b2129d85-b113-4edf-b1bb-797761ca79c3;
					- m_sourceType = 'F';
					- m_pTarget = GUID 0cbf5c16-943e-4648-92d5-0c3d1d5f2917;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 1 1066 245  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 1142 1046 ;
					- m_TargetPort = 706 156 ;
					- m_bShowKeyword = 1;
					- m_showConveyed = name;
					- m_keyword = { CGIText 
						- m_str = "\쳀low\�";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  48 -9  48 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 1074 393 ;
						- m_nHorizontalSpacing = 49;
						- m_nVerticalSpacing = 89;
						- m_nOrientationCtrlPt = 8;
					}
					- m_conveyed = { CGIText 
						- m_str = "EN_PINS";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -33 -8  39 -8  39 10  -33 10  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 1101 416 ;
						- m_nHorizontalSpacing = -13;
						- m_nVerticalSpacing = 113;
						- m_nOrientationCtrlPt = 7;
					}
					- m_direction = type_122;
				}
				{ CGIInformationFlow 
					- _id = GUID b6401af2-6e72-4995-9978-3a54a02f8274;
					- m_type = 180;
					- m_pModelObject = { IHandle 
						- _m2Class = "IInformationFlow";
						- _filename = "Sources.sbs";
						- _subsystem = "Sources";
						- _class = "";
						- _name = "GPIO_Driver_0";
						- _id = GUID 5ffc4af5-af71-4933-9ca5-fadda02edfad;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID b2129d85-b113-4edf-b1bb-797761ca79c3;
					- m_sourceType = 'F';
					- m_pTarget = GUID 8c264ffe-3b7b-4166-9774-453259715c57;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 3 588 253  588 300  433 300  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 9 1202 ;
					- m_TargetPort = 821 10 ;
					- m_bShowKeyword = 1;
					- m_showConveyed = name;
					- m_keyword = { CGIText 
						- m_str = "\쳀low\�";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  48 -9  48 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 558 309 ;
						- m_nHorizontalSpacing = -25;
						- m_nVerticalSpacing = 37;
						- m_nOrientationCtrlPt = 8;
					}
					- m_conveyed = { CGIText 
						- m_str = "EN_PINS";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -33 -8  39 -8  39 10  -33 10  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 525 308 ;
						- m_nHorizontalSpacing = -112;
						- m_nVerticalSpacing = 72;
						- m_nOrientationCtrlPt = 7;
					}
					- m_direction = type_122;
				}
				
				- m_access = 'Z';
				- m_modified = 'N';
				- m_fileVersion = "";
				- m_nModifyDate = 0;
				- m_nCreateDate = 0;
				- m_creator = "";
				- m_bScaleWithZoom = 1;
				- m_arrowStyle = 'S';
				- m_pRoot = GUID 80730c39-2911-414c-8de5-60d13e2002eb;
				- m_currentLeftTop = 0 0 ;
				- m_currentRightBottom = 0 0 ;
			}
			- _defaultSubsystem = { IHandle 
				- _m2Class = "ISubsystem";
				- _filename = "Sources.sbs";
				- _subsystem = "";
				- _class = "";
				- _name = "Sources";
				- _id = GUID f9623802-9e64-4088-b484-572be495c316;
			}
		}
		{ IDiagram 
			- _id = GUID c745a580-9e49-477a-b69d-9fed186430f0;
			- _myState = 8192;
			- _properties = { IPropertyContainer 
				- Subjects = { IRPYRawContainer 
					- size = 3;
					- value = 
					{ IPropertySubject 
						- _Name = "Format";
						- Metaclasses = { IRPYRawContainer 
							- size = 9;
							- value = 
							{ IPropertyMetaclass 
								- _Name = "Anchor";
								- Properties = { IRPYRawContainer 
									- size = 6;
									- value = 
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "0,0,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineStyle";
										- _Value = "1";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "0";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "Class";
								- Properties = { IRPYRawContainer 
									- size = 8;
									- value = 
									{ IProperty 
										- _Name = "DefaultSize";
										- _Value = "0,34,84,148";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Fill.FillColor";
										- _Value = "255,255,255";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "121,122,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineStyle";
										- _Value = "0";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "Comment";
								- Properties = { IRPYRawContainer 
									- size = 7;
									- value = 
									{ IProperty 
										- _Name = "DefaultSize";
										- _Value = "0,0,84,96";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Fill.FillColor";
										- _Value = "255,255,207";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "225,225,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "Component";
								- Properties = { IRPYRawContainer 
									- size = 7;
									- value = 
									{ IProperty 
										- _Name = "DefaultSize";
										- _Value = "0,0,276,180";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Fill.FillColor";
										- _Value = "255,255,255";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "0,16,230";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "Depends";
								- Properties = { IRPYRawContainer 
									- size = 6;
									- value = 
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,128";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "0,16,230";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineStyle";
										- _Value = "1";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "0";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "FreeText";
								- Properties = { IRPYRawContainer 
									- size = 9;
									- value = 
									{ IProperty 
										- _Name = "Fill.Transparent_Fill";
										- _Value = "1";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.Height";
										- _Value = "13";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "HorzAlign";
										- _Value = "0";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.Transparent";
										- _Value = "1";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Multiline";
										- _Value = "True";
										- _Type = Bool;
									}
									{ IProperty 
										- _Name = "VertAlign";
										- _Value = "0";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Wordbreak";
										- _Value = "False";
										- _Type = Bool;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "Polyline";
								- Properties = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "0";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "Rectangle";
								- Properties = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "0";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "Requirement";
								- Properties = { IRPYRawContainer 
									- size = 7;
									- value = 
									{ IProperty 
										- _Name = "DefaultSize";
										- _Value = "0,0,84,96";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Fill.FillColor";
										- _Value = "255,255,207";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "225,225,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
						}
					}
					{ IPropertySubject 
						- _Name = "General";
						- Metaclasses = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertyMetaclass 
								- _Name = "Graphics";
								- Properties = { IRPYRawContainer 
									- size = 2;
									- value = 
									{ IProperty 
										- _Name = "grid_display";
										- _Value = "False";
										- _Type = Bool;
									}
									{ IProperty 
										- _Name = "grid_snap";
										- _Value = "True";
										- _Type = Bool;
									}
								}
							}
						}
					}
					{ IPropertySubject 
						- _Name = "ObjectModelGe";
						- Metaclasses = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertyMetaclass 
								- _Name = "ClassDiagram";
								- Properties = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IProperty 
										- _Name = "Fillcolor";
										- _Value = "192,192,192";
										- _Type = Color;
									}
								}
							}
						}
					}
				}
			}
			- _name = "requirements";
			- _objectCreation = "59175152546201610308591159";
			- _umlDependencyID = "3020";
			- _lastModifiedTime = "11.5.2016::18:50:47";
			- _graphicChart = { CGIClassChart 
				- _id = GUID 1e1f683c-3117-43aa-9e5b-d696ba919192;
				- m_type = 0;
				- m_pModelObject = { IHandle 
					- _m2Class = "IDiagram";
					- _id = GUID c745a580-9e49-477a-b69d-9fed186430f0;
				}
				- m_pParent = ;
				- m_name = { CGIText 
					- m_str = "";
					- m_style = "Arial" 10 0 0 0 1 ;
					- m_color = { IColor 
						- m_fgColor = 0;
						- m_bgColor = 0;
						- m_bgFlag = 0;
					}
					- m_position = 1 0 0  ;
					- m_nIdent = 0;
					- m_bImplicitSetRectPoints = 0;
					- m_nOrientationCtrlPt = 8;
				}
				- m_drawBehavior = 0;
				- m_bIsPreferencesInitialized = 0;
				- elementList = 58;
				{ CGIClass 
					- _id = GUID 46f67643-04ce-4ad1-b869-81e9432f9a65;
					- m_type = 78;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "Sources.sbs";
						- _subsystem = "Sources";
						- _class = "";
						- _name = "TopLevel";
						- _id = GUID c96d5194-58ed-4182-82e6-04845c227d30;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "TopLevel";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 0;
					- m_bIsPreferencesInitialized = 0;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 0 ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Attrs = { IRPYRawContainer 
						- size = 0;
					}
					- Operations = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIAnnotation 
					- _id = GUID fcaa826e-2f8a-4a57-b220-de2c1c9574a6;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 173;
					- m_pModelObject = { IHandle 
						- _m2Class = "IComment";
						- _filename = "System.sbs";
						- _subsystem = "System";
						- _class = "";
						- _name = "comment_3";
						- _id = GUID bcfd6366-23a8-4378-aacc-993db9993486;
					}
					- m_pParent = GUID 46f67643-04ce-4ad1-b869-81e9432f9a65;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.430812 0 0 0.0879121 120 23.7363 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 0 3  0 1095  1084 1095  1084 3  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- _iTempdisplayTextFlag = 2;
					- m_bIsBoxStyle = 0;
				}
				{ CGIAnnotation 
					- _id = GUID 12bcbe5b-0dfe-4770-9fd0-c05505219122;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
							{ IPropertySubject 
								- _Name = "ObjectModelGe";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Requirement";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "Compartments";
												- _Value = "ID,Specification";
												- _Type = MultiLine;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 176;
					- m_pModelObject = { IHandle 
						- _m2Class = "IRequirement";
						- _filename = "Requirements.sbs";
						- _subsystem = "Requirements";
						- _class = "";
						- _name = "HLR AutoCal";
						- _id = GUID e93f544b-e8c9-4aa8-a8bc-9d66a3a0609e;
					}
					- m_pParent = GUID 46f67643-04ce-4ad1-b869-81e9432f9a65;
					- m_name = { CGIText 
						- m_str = "HLR AutoCal";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.164921 0 0 0.196837 252 288.463 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 0 3  0 1095  1084 1095  1084 3  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=33%,67%>
<frame name=IDTextCompartment>
<frame name=SpecificationTextCompartment>";
					- _iTempdisplayTextFlag = 1;
					- m_bIsBoxStyle = 1;
				}
				{ CGIAnnotation 
					- _id = GUID 69698467-e688-4c21-82db-b66d4a06ab9d;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
							{ IPropertySubject 
								- _Name = "ObjectModelGe";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Requirement";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "Compartments";
												- _Value = "ID,Specification";
												- _Type = MultiLine;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 176;
					- m_pModelObject = { IHandle 
						- _m2Class = "IRequirement";
						- _filename = "Requirements.sbs";
						- _subsystem = "Requirements";
						- _class = "";
						- _name = "HLR Commands";
						- _id = GUID 460e3aa9-978f-466f-8789-626a78b7423b;
					}
					- m_pParent = GUID 46f67643-04ce-4ad1-b869-81e9432f9a65;
					- m_name = { CGIText 
						- m_str = "HLR Commands";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.165853 0 0 0.196837 1272.05 288.463 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 0 3  0 1095  1084 1095  1084 3  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=33%,67%>
<frame name=IDTextCompartment>
<frame name=SpecificationTextCompartment>";
					- _iTempdisplayTextFlag = 2;
					- m_bIsBoxStyle = 1;
				}
				{ CGIAnnotation 
					- _id = GUID 461d89a7-6d35-4cde-a3b8-b00ba530b394;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
							{ IPropertySubject 
								- _Name = "ObjectModelGe";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Requirement";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "Compartments";
												- _Value = "ID,Specification";
												- _Type = MultiLine;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 176;
					- m_pModelObject = { IHandle 
						- _m2Class = "IRequirement";
						- _filename = "Requirements.sbs";
						- _subsystem = "Requirements";
						- _class = "";
						- _name = "HLR Diagnostics";
						- _id = GUID 42655265-2c52-4a0d-bd17-39fd3dc763f2;
					}
					- m_pParent = GUID 46f67643-04ce-4ad1-b869-81e9432f9a65;
					- m_name = { CGIText 
						- m_str = "HLR Diagnostics";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.164921 0 0 0.196837 456.09 288.463 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 0 3  0 1095  1084 1095  1084 3  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=39%,61%>
<frame name=IDTextCompartment>
<frame name=SpecificationTextCompartment>";
					- _iTempdisplayTextFlag = 2;
					- m_bIsBoxStyle = 1;
				}
				{ CGIAnnotation 
					- _id = GUID da6596ea-f299-42fa-844f-14a404363059;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
							{ IPropertySubject 
								- _Name = "ObjectModelGe";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Requirement";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "Compartments";
												- _Value = "ID,Specification";
												- _Type = MultiLine;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 176;
					- m_pModelObject = { IHandle 
						- _m2Class = "IRequirement";
						- _filename = "Requirements.sbs";
						- _subsystem = "Requirements";
						- _class = "";
						- _name = "HLR Follow";
						- _id = GUID 304ee28a-86d1-4eb4-93a1-eac2600b0ed0;
					}
					- m_pParent = GUID 46f67643-04ce-4ad1-b869-81e9432f9a65;
					- m_name = { CGIText 
						- m_str = "HLR Follow";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.164921 0 0 0.196837 864.135 288.463 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 0 3  0 1095  1084 1095  1084 3  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=28%,72%>
<frame name=IDTextCompartment>
<frame name=SpecificationTextCompartment>";
					- _iTempdisplayTextFlag = 2;
					- m_bIsBoxStyle = 1;
				}
				{ CGIAnnotation 
					- _id = GUID d27813b2-f5fc-41c6-a237-c66f885c998f;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
							{ IPropertySubject 
								- _Name = "ObjectModelGe";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Requirement";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "Compartments";
												- _Value = "ID,Specification";
												- _Type = MultiLine;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 176;
					- m_pModelObject = { IHandle 
						- _m2Class = "IRequirement";
						- _filename = "Requirements.sbs";
						- _subsystem = "Requirements";
						- _class = "";
						- _name = "HLR IR Array";
						- _id = GUID 121d8adf-2f89-4e88-b86b-b2c309931f3d;
					}
					- m_pParent = GUID 46f67643-04ce-4ad1-b869-81e9432f9a65;
					- m_name = { CGIText 
						- m_str = "HLR IR Array";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.164921 0 0 0.196837 1068.18 288.463 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 0 3  0 1095  1084 1095  1084 3  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=33%,67%>
<frame name=IDTextCompartment>
<frame name=SpecificationTextCompartment>";
					- _iTempdisplayTextFlag = 2;
					- m_bIsBoxStyle = 1;
				}
				{ CGIAnnotation 
					- _id = GUID 8bedf126-30f1-4667-9c53-200b088882c8;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
							{ IPropertySubject 
								- _Name = "ObjectModelGe";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Requirement";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "Compartments";
												- _Value = "ID,Specification";
												- _Type = MultiLine;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 176;
					- m_pModelObject = { IHandle 
						- _m2Class = "IRequirement";
						- _filename = "Requirements.sbs";
						- _subsystem = "Requirements";
						- _class = "";
						- _name = "HLR Untethered";
						- _id = GUID 86c7f850-9d8b-4412-bbc6-b221d80a4cd4;
					}
					- m_pParent = GUID 46f67643-04ce-4ad1-b869-81e9432f9a65;
					- m_name = { CGIText 
						- m_str = "HLR Untethered";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.164921 0 0 0.196837 660.226 288.463 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_bFramesetModified = 1;
					- m_polygon = 4 0 3  0 1095  1084 1095  1084 3  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=19%,81%>
<frame name=IDTextCompartment>
<frame name=SpecificationTextCompartment>";
					- _iTempdisplayTextFlag = 2;
					- m_bIsBoxStyle = 1;
				}
				{ CGIAnnotation 
					- _id = GUID 8f24f3e5-c603-4185-be79-17655a7dd49a;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 173;
					- m_pModelObject = { IHandle 
						- _m2Class = "IComment";
						- _filename = "System.sbs";
						- _subsystem = "System";
						- _class = "";
						- _name = "comment_9";
						- _id = GUID 96f69553-5a93-44f1-a7e8-4cfc3a91b642;
					}
					- m_pParent = GUID 46f67643-04ce-4ad1-b869-81e9432f9a65;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.099631 0 0 0.0549451 1152 131.835 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 0 3  0 1095  1084 1095  1084 3  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- _iTempdisplayTextFlag = 2;
					- m_bIsBoxStyle = 0;
				}
				{ CGIAnnotation 
					- _id = GUID fca3e041-95a3-4a7e-ba53-dc2458ed10df;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
							{ IPropertySubject 
								- _Name = "ObjectModelGe";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Requirement";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "Compartments";
												- _Value = "ID,Specification";
												- _Type = MultiLine;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 176;
					- m_pModelObject = { IHandle 
						- _m2Class = "IRequirement";
						- _filename = "Requirements.sbs";
						- _subsystem = "Requirements";
						- _class = "";
						- _name = "LLR Cal BG";
						- _id = GUID 8ac0aefc-c444-4f97-afd0-4c0c24891896;
					}
					- m_pParent = GUID 46f67643-04ce-4ad1-b869-81e9432f9a65;
					- m_name = { CGIText 
						- m_str = "LLR Cal BG";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.132737 0 0 0.152853 84 624.662 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_bFramesetModified = 1;
					- m_polygon = 4 0 3  0 1095  1084 1095  1084 3  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=26%,74%>
<frame name=IDTextCompartment>
<frame name=SpecificationTextCompartment>";
					- _iTempdisplayTextFlag = 2;
					- m_bIsBoxStyle = 1;
				}
				{ CGIAnnotation 
					- _id = GUID 9ff661d4-d8ca-48ee-aa96-4c5548b78ef8;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
							{ IPropertySubject 
								- _Name = "ObjectModelGe";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Requirement";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "Compartments";
												- _Value = "ID,Specification";
												- _Type = MultiLine;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 176;
					- m_pModelObject = { IHandle 
						- _m2Class = "IRequirement";
						- _filename = "Requirements.sbs";
						- _subsystem = "Requirements";
						- _class = "";
						- _name = "LLR Cal Max";
						- _id = GUID 531e45e7-14af-474f-be50-d00ec60031d4;
					}
					- m_pParent = GUID 46f67643-04ce-4ad1-b869-81e9432f9a65;
					- m_name = { CGIText 
						- m_str = "LLR Cal Max";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.133658 0 0 0.152946 83.9072 804.524 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 0 3  0 1095  1084 1095  1084 3  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=33%,67%>
<frame name=IDTextCompartment>
<frame name=SpecificationTextCompartment>";
					- _iTempdisplayTextFlag = 2;
					- m_bIsBoxStyle = 1;
				}
				{ CGIAnnotation 
					- _id = GUID bcda1f91-c486-407a-a4ee-10b09ba9da3a;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
							{ IPropertySubject 
								- _Name = "ObjectModelGe";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Requirement";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "Compartments";
												- _Value = "ID,Specification";
												- _Type = MultiLine;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 176;
					- m_pModelObject = { IHandle 
						- _m2Class = "IRequirement";
						- _filename = "Requirements.sbs";
						- _subsystem = "Requirements";
						- _class = "";
						- _name = "LLR Cal Min";
						- _id = GUID ced9d27b-3353-4648-acd2-22cc14a12654;
					}
					- m_pParent = GUID 46f67643-04ce-4ad1-b869-81e9432f9a65;
					- m_name = { CGIText 
						- m_str = "LLR Cal Min";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.133733 0 0 0.152918 84.2187 984.528 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 0 3  0 1095  1084 1095  1084 3  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=33%,67%>
<frame name=IDTextCompartment>
<frame name=SpecificationTextCompartment>";
					- _iTempdisplayTextFlag = 2;
					- m_bIsBoxStyle = 1;
				}
				{ CGIAnnotation 
					- _id = GUID a94825f0-fceb-4f3c-8da3-5f1993948dea;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
							{ IPropertySubject 
								- _Name = "ObjectModelGe";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Requirement";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "Compartments";
												- _Value = "ID,Specification";
												- _Type = MultiLine;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 176;
					- m_pModelObject = { IHandle 
						- _m2Class = "IRequirement";
						- _filename = "Requirements.sbs";
						- _subsystem = "Requirements";
						- _class = "";
						- _name = "LLR Follow Error";
						- _id = GUID c952fe60-9873-4148-8ee3-2a9d770ce1c4;
					}
					- m_pParent = GUID 46f67643-04ce-4ad1-b869-81e9432f9a65;
					- m_name = { CGIText 
						- m_str = "LLR Follow Error";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.133733 0 0 0.141517 803.633 624.629 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 0 3  0 1095  1084 1095  1084 3  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=39%,61%>
<frame name=IDTextCompartment>
<frame name=SpecificationTextCompartment>";
					- _iTempdisplayTextFlag = 2;
					- m_bIsBoxStyle = 1;
				}
				{ CGIAnnotation 
					- _id = GUID f73de7ee-ef50-495c-b792-05f331a08389;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
							{ IPropertySubject 
								- _Name = "ObjectModelGe";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Requirement";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "Compartments";
												- _Value = "ID,Specification";
												- _Type = MultiLine;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 176;
					- m_pModelObject = { IHandle 
						- _m2Class = "IRequirement";
						- _filename = "Requirements.sbs";
						- _subsystem = "Requirements";
						- _class = "";
						- _name = "LLR Follow PID";
						- _id = GUID c6ef3037-019e-45db-a3d5-4e798d15e707;
					}
					- m_pParent = GUID 46f67643-04ce-4ad1-b869-81e9432f9a65;
					- m_name = { CGIText 
						- m_str = "LLR Follow PID";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.133733 0 0 0.141517 983.545 624.843 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 0 3  0 1095  1084 1095  1084 3  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=39%,61%>
<frame name=IDTextCompartment>
<frame name=SpecificationTextCompartment>";
					- _iTempdisplayTextFlag = 2;
					- m_bIsBoxStyle = 1;
				}
				{ CGIAnnotation 
					- _id = GUID b3cd0bd7-0aac-4e8a-af68-99e602874af1;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
							{ IPropertySubject 
								- _Name = "ObjectModelGe";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Requirement";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "Compartments";
												- _Value = "ID,Specification";
												- _Type = MultiLine;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 176;
					- m_pModelObject = { IHandle 
						- _m2Class = "IRequirement";
						- _filename = "Requirements.sbs";
						- _subsystem = "Requirements";
						- _class = "";
						- _name = "LLR Speed Driver";
						- _id = GUID a5d683ae-3d5d-46ff-a393-cb891f8d1d25;
					}
					- m_pParent = GUID 46f67643-04ce-4ad1-b869-81e9432f9a65;
					- m_name = { CGIText 
						- m_str = "LLR Speed Driver";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.133733 0 0 0.153574 1392.21 624.404 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_bFramesetModified = 1;
					- m_polygon = 4 0 3  0 1095  1084 1095  1084 3  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=26%,74%>
<frame name=IDTextCompartment>
<frame name=SpecificationTextCompartment>";
					- _iTempdisplayTextFlag = 2;
					- m_bIsBoxStyle = 1;
				}
				{ CGIAnnotation 
					- _id = GUID 4d546175-a448-4398-bde5-e6e27a87f661;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
							{ IPropertySubject 
								- _Name = "ObjectModelGe";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Requirement";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "Compartments";
												- _Value = "ID,Specification";
												- _Type = MultiLine;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 176;
					- m_pModelObject = { IHandle 
						- _m2Class = "IRequirement";
						- _filename = "Requirements.sbs";
						- _subsystem = "Requirements";
						- _class = "";
						- _name = "LLR Speed Measure";
						- _id = GUID 50b07cd5-2555-4deb-a638-4865c060f9f5;
					}
					- m_pParent = GUID 46f67643-04ce-4ad1-b869-81e9432f9a65;
					- m_name = { CGIText 
						- m_str = "LLR Speed Measure";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.133658 0 0 0.152946 1584.12 624.524 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 0 3  0 1095  1084 1095  1084 3  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=33%,67%>
<frame name=IDTextCompartment>
<frame name=SpecificationTextCompartment>";
					- _iTempdisplayTextFlag = 2;
					- m_bIsBoxStyle = 1;
				}
				{ CGIAnnotation 
					- _id = GUID deea7463-a4a2-4ce3-9040-35d0d16757e0;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
							{ IPropertySubject 
								- _Name = "ObjectModelGe";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Requirement";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "Compartments";
												- _Value = "ID,Specification";
												- _Type = MultiLine;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 176;
					- m_pModelObject = { IHandle 
						- _m2Class = "IRequirement";
						- _filename = "Requirements.sbs";
						- _subsystem = "Requirements";
						- _class = "";
						- _name = "LLR Speed PID";
						- _id = GUID 8f884294-033d-4590-bcc4-5db67ad55ed6;
					}
					- m_pParent = GUID 46f67643-04ce-4ad1-b869-81e9432f9a65;
					- m_name = { CGIText 
						- m_str = "LLR Speed PID";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.133733 0 0 0.152918 1488.03 804.554 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 0 3  0 1095  1084 1095  1084 3  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=33%,67%>
<frame name=IDTextCompartment>
<frame name=SpecificationTextCompartment>";
					- _iTempdisplayTextFlag = 2;
					- m_bIsBoxStyle = 1;
				}
				{ CGIAnnotation 
					- _id = GUID 5b9eb42f-61b2-4772-b081-d9dd8e231fcd;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
							{ IPropertySubject 
								- _Name = "ObjectModelGe";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Requirement";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "Compartments";
												- _Value = "ID,Specification";
												- _Type = MultiLine;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 176;
					- m_pModelObject = { IHandle 
						- _m2Class = "IRequirement";
						- _filename = "Requirements.sbs";
						- _subsystem = "Requirements";
						- _class = "";
						- _name = "HLR Speed";
						- _id = GUID d3da3843-61c5-4766-b364-0d434eadf304;
					}
					- m_pParent = GUID 46f67643-04ce-4ad1-b869-81e9432f9a65;
					- m_name = { CGIText 
						- m_str = "HLR Speed";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.166052 0 0 0.196837 1476 288.463 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 0 3  0 1095  1084 1095  1084 3  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=39%,61%>
<frame name=IDTextCompartment>
<frame name=SpecificationTextCompartment>";
					- _iTempdisplayTextFlag = 2;
					- m_bIsBoxStyle = 1;
				}
				{ CGIAnnotation 
					- _id = GUID 42a38364-66d8-4c04-bbd4-a84507ec8ff3;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
							{ IPropertySubject 
								- _Name = "ObjectModelGe";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Requirement";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "Compartments";
												- _Value = "ID,Specification";
												- _Type = MultiLine;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 176;
					- m_pModelObject = { IHandle 
						- _m2Class = "IRequirement";
						- _filename = "Requirements.sbs";
						- _subsystem = "Requirements";
						- _class = "";
						- _name = "LLR Diag Encoder";
						- _id = GUID 15cdda37-ae7f-43f8-ba18-a9cc0e328915;
					}
					- m_pParent = GUID 46f67643-04ce-4ad1-b869-81e9432f9a65;
					- m_name = { CGIText 
						- m_str = "LLR Diag Encoder";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.133733 0 0 0.15235 371.52 624.868 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_bFramesetModified = 1;
					- m_polygon = 4 0 3  0 1095  1084 1095  1084 3  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=25%,75%>
<frame name=IDTextCompartment>
<frame name=SpecificationTextCompartment>";
					- _iTempdisplayTextFlag = 2;
					- m_bIsBoxStyle = 1;
				}
				{ CGIAnnotation 
					- _id = GUID 461ca06a-8fb8-4756-8cd5-1119dff648fd;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
							{ IPropertySubject 
								- _Name = "ObjectModelGe";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Requirement";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "Compartments";
												- _Value = "ID,Specification";
												- _Type = MultiLine;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 176;
					- m_pModelObject = { IHandle 
						- _m2Class = "IRequirement";
						- _filename = "Requirements.sbs";
						- _subsystem = "Requirements";
						- _class = "";
						- _name = "LLR Diag IR";
						- _id = GUID 061f2cf0-1412-4cb9-8c31-190f83219294;
					}
					- m_pParent = GUID 46f67643-04ce-4ad1-b869-81e9432f9a65;
					- m_name = { CGIText 
						- m_str = "LLR Diag IR";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.133733 0 0 0.152736 576.432 624.805 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 0 3  0 1095  1084 1095  1084 3  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=39%,61%>
<frame name=IDTextCompartment>
<frame name=SpecificationTextCompartment>";
					- _iTempdisplayTextFlag = 2;
					- m_bIsBoxStyle = 1;
				}
				{ CGIAnnotation 
					- _id = GUID e3b90614-edc1-47fb-acf2-78d7b7bc751c;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
							{ IPropertySubject 
								- _Name = "ObjectModelGe";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Requirement";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "Compartments";
												- _Value = "ID,Specification";
												- _Type = MultiLine;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 176;
					- m_pModelObject = { IHandle 
						- _m2Class = "IRequirement";
						- _filename = "Requirements.sbs";
						- _subsystem = "Requirements";
						- _class = "";
						- _name = "LLR Diag Log";
						- _id = GUID bff51acd-8dfa-4bae-81a9-a42749f9bc13;
					}
					- m_pParent = GUID 46f67643-04ce-4ad1-b869-81e9432f9a65;
					- m_name = { CGIText 
						- m_str = "LLR Diag Log";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.133733 0 0 0.152736 372.343 804.908 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 0 3  0 1095  1084 1095  1084 3  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=39%,61%>
<frame name=IDTextCompartment>
<frame name=SpecificationTextCompartment>";
					- _iTempdisplayTextFlag = 2;
					- m_bIsBoxStyle = 1;
				}
				{ CGIAnnotation 
					- _id = GUID 12636374-a1cc-4001-b28b-c2830342e8cb;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
							{ IPropertySubject 
								- _Name = "ObjectModelGe";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Requirement";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "Compartments";
												- _Value = "ID,Specification";
												- _Type = MultiLine;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 176;
					- m_pModelObject = { IHandle 
						- _m2Class = "IRequirement";
						- _filename = "Requirements.sbs";
						- _subsystem = "Requirements";
						- _class = "";
						- _name = "LLR Diag Motor";
						- _id = GUID 8f95f975-89fb-4e59-ab9e-ac4946b945a6;
					}
					- m_pParent = GUID 46f67643-04ce-4ad1-b869-81e9432f9a65;
					- m_name = { CGIText 
						- m_str = "LLR Diag Motor";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.133733 0 0 0.152959 576.255 804.895 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 0 3  0 1095  1084 1095  1084 3  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=49%,51%>
<frame name=IDTextCompartment>
<frame name=SpecificationTextCompartment>";
					- _iTempdisplayTextFlag = 2;
					- m_bIsBoxStyle = 1;
				}
				{ CGIAnnotation 
					- _id = GUID 67c8cc3c-5905-4426-b2a3-e94fcaa9af98;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
							{ IPropertySubject 
								- _Name = "ObjectModelGe";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Requirement";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "Compartments";
												- _Value = "ID,Specification";
												- _Type = MultiLine;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 176;
					- m_pModelObject = { IHandle 
						- _m2Class = "IRequirement";
						- _filename = "Requirements.sbs";
						- _subsystem = "Requirements";
						- _class = "";
						- _name = "LLR Sensors";
						- _id = GUID d7a220c3-edde-4075-81f4-b2eabd44cf33;
					}
					- m_pParent = GUID 46f67643-04ce-4ad1-b869-81e9432f9a65;
					- m_name = { CGIText 
						- m_str = "LLR Sensors";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.133733 0 0 0.141802 1163.91 624.799 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 0 3  0 1095  1084 1095  1084 3  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=39%,61%>
<frame name=IDTextCompartment>
<frame name=SpecificationTextCompartment>";
					- _iTempdisplayTextFlag = 2;
					- m_bIsBoxStyle = 1;
				}
				{ CGIInheritance 
					- _id = GUID 337d2e35-9f0c-4795-bbb9-9426c5c479f0;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "Requirements.sbs";
						- _subsystem = "Requirements";
						- _class = "";
						- _name = "LLR Sensors";
						- _id = GUID 339bf44f-b6d2-45dc-8815-eea3df3b85d1;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "LLR Sensors";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID d27813b2-f5fc-41c6-a237-c66f885c998f;
					- m_sourceType = 'F';
					- m_pTarget = GUID 67c8cc3c-5905-4426-b2a3-e94fcaa9af98;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "derive";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  62 -9  62 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 1122 573 ;
						- m_nHorizontalSpacing = -16;
						- m_nVerticalSpacing = 8;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 508 1095 ;
					- m_TargetPort = 360 -6 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID 53731de9-9e92-4972-842a-ca832a659be7;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "Requirements.sbs";
						- _subsystem = "Requirements";
						- _class = "";
						- _name = "LLR Sensors";
						- _id = GUID 409315b2-d446-4b09-991f-8253f8fe653c;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "LLR Sensors";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 69698467-e688-4c21-82db-b66d4a06ab9d;
					- m_sourceType = 'F';
					- m_pTarget = GUID 67c8cc3c-5905-4426-b2a3-e94fcaa9af98;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "derive";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  62 -9  62 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 1314 573 ;
						- m_nHorizontalSpacing = 38;
						- m_nVerticalSpacing = 5;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 542 1080 ;
					- m_TargetPort = 719 -6 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID 4f4a6d9d-fa0e-45e1-a829-c34601e28298;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "Requirements.sbs";
						- _subsystem = "Requirements";
						- _class = "";
						- _name = "LLR Speed Driver";
						- _id = GUID cb5d2d38-ba99-442b-846b-d27248b10b06;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "LLR Speed Driver";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8192;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 5b9eb42f-61b2-4772-b081-d9dd8e231fcd;
					- m_sourceType = 'F';
					- m_pTarget = GUID b3cd0bd7-0aac-4e8a-af68-99e602874af1;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "derive";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  62 -9  62 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 1446 573 ;
						- m_nHorizontalSpacing = -13;
						- m_nVerticalSpacing = 15;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 157 1080 ;
					- m_TargetPort = 821 -9 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID 989943e4-6db2-406a-8ba5-684ab8c399bd;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "Requirements.sbs";
						- _subsystem = "Requirements";
						- _class = "";
						- _name = "LLR Speed Measure";
						- _id = GUID c4ddb24b-924d-4159-8dec-54b0a8fe82cf;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "LLR Speed Measure";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8192;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 5b9eb42f-61b2-4772-b081-d9dd8e231fcd;
					- m_sourceType = 'F';
					- m_pTarget = GUID 4d546175-a448-4398-bde5-e6e27a87f661;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "derive";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  62 -9  62 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 1626 573 ;
						- m_nHorizontalSpacing = 47;
						- m_nVerticalSpacing = 15;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 879 1080 ;
					- m_TargetPort = 283 3 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID f1cc9db7-ee7f-4ed2-8de4-67b6adfce62d;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "Requirements.sbs";
						- _subsystem = "Requirements";
						- _class = "";
						- _name = "LLR Speed PID";
						- _id = GUID a21ead0c-d20d-4098-b628-687e44e0c0fe;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "LLR Speed PID";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8192;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 5b9eb42f-61b2-4772-b081-d9dd8e231fcd;
					- m_sourceType = 'F';
					- m_pTarget = GUID deea7463-a4a2-4ce3-9040-35d0d16757e0;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "derive";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  62 -9  62 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 1506 573 ;
						- m_nHorizontalSpacing = -11;
						- m_nVerticalSpacing = -66;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 506 1034 ;
					- m_TargetPort = 538 36 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID ceeee5aa-a90d-4f31-91dd-301342676081;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "Requirements.sbs";
						- _subsystem = "Requirements";
						- _class = "";
						- _name = "LLR Follow PID";
						- _id = GUID 72a7d4bc-a4cd-4e34-a89b-a457c6a9d607;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "LLR Follow PID";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID da6596ea-f299-42fa-844f-14a404363059;
					- m_sourceType = 'F';
					- m_pTarget = GUID f73de7ee-ef50-495c-b792-05f331a08389;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "derive";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  62 -9  62 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 1026 573 ;
						- m_nHorizontalSpacing = 58;
						- m_nVerticalSpacing = 15;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 891 1075 ;
					- m_TargetPort = 205 15 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID 7323939c-8fe5-4dde-9090-41b62dc40c4f;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "Requirements.sbs";
						- _subsystem = "Requirements";
						- _class = "";
						- _name = "LLR Follow Error";
						- _id = GUID 499bd0a7-3482-480c-89c0-13b5a7a7b715;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "LLR Follow Error";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID da6596ea-f299-42fa-844f-14a404363059;
					- m_sourceType = 'F';
					- m_pTarget = GUID a94825f0-fceb-4f3c-8da3-5f1993948dea;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "derive";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  62 -9  62 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 846 573 ;
						- m_nHorizontalSpacing = -23;
						- m_nVerticalSpacing = 15;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 290 1034 ;
					- m_TargetPort = 810 356 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID 73ef50b4-822a-423e-9317-c4429deafaab;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "Requirements.sbs";
						- _subsystem = "Requirements";
						- _class = "";
						- _name = "LLR Diag IR";
						- _id = GUID c3f5776b-a82c-4c11-bafd-08b2ba2aeed0;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "LLR Diag IR";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 461d89a7-6d35-4cde-a3b8-b00ba530b394;
					- m_sourceType = 'F';
					- m_pTarget = GUID 461ca06a-8fb8-4756-8cd5-1119dff648fd;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "derive";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  62 -9  62 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 618 573 ;
						- m_nHorizontalSpacing = 47;
						- m_nVerticalSpacing = 15;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 957 1090 ;
					- m_TargetPort = 281 73 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID be2db69d-9138-4cf2-9492-62155ef2b640;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "Requirements.sbs";
						- _subsystem = "Requirements";
						- _class = "";
						- _name = "LLR Diag Encoder";
						- _id = GUID 8fc29086-7b51-499f-bd03-8b05de3fdc52;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "LLR Diag Encoder";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 461d89a7-6d35-4cde-a3b8-b00ba530b394;
					- m_sourceType = 'F';
					- m_pTarget = GUID 42a38364-66d8-4c04-bbd4-a84507ec8ff3;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "derive";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  62 -9  62 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 426 573 ;
						- m_nHorizontalSpacing = -14;
						- m_nVerticalSpacing = 15;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 163 1090 ;
					- m_TargetPort = 834 106 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID e98ab180-52c0-4f16-b794-ca6b29c95b99;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "Requirements.sbs";
						- _subsystem = "Requirements";
						- _class = "";
						- _name = "LLR Diag Motor";
						- _id = GUID ec72f246-29c7-40c9-9ec1-8ad0b1dff387;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "LLR Diag Motor";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 461d89a7-6d35-4cde-a3b8-b00ba530b394;
					- m_sourceType = 'F';
					- m_pTarget = GUID 12636374-a1cc-4001-b28b-c2830342e8cb;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "derive";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  62 -9  62 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 558 501 ;
						- m_nHorizontalSpacing = 48;
						- m_nVerticalSpacing = -97;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 1 553 900  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 588 1095 ;
					- m_TargetPort = -2 622 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID 936e4477-58a2-4d3f-911f-51ba94d3e3ee;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "Requirements.sbs";
						- _subsystem = "Requirements";
						- _class = "";
						- _name = "LLR Diag Log";
						- _id = GUID 3bfb0341-fa34-4aa2-8fe6-7819253aa23e;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "LLR Diag Log";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 461d89a7-6d35-4cde-a3b8-b00ba530b394;
					- m_sourceType = 'F';
					- m_pTarget = GUID e3b90614-edc1-47fb-acf2-78d7b7bc751c;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "derive";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  62 -9  62 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 486 501 ;
						- m_nHorizontalSpacing = -11;
						- m_nVerticalSpacing = -97;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 1 540 899  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 509 1034 ;
					- m_TargetPort = 1022 616 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID aede800e-c9ee-453a-a037-e9ba516f5672;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "Requirements.sbs";
						- _subsystem = "Requirements";
						- _class = "";
						- _name = "LLR Cal BG";
						- _id = GUID 3aae3d9d-2528-4d16-a0c5-3ae5b8cae463;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "LLR Cal BG";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 12bcbe5b-0dfe-4770-9fd0-c05505219122;
					- m_sourceType = 'F';
					- m_pTarget = GUID fca3e041-95a3-4a7e-ba53-dc2458ed10df;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "derive";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  62 -9  62 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 162 561 ;
						- m_nHorizontalSpacing = -17;
						- m_nVerticalSpacing = 7;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 1 263 660  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 67 1065 ;
					- m_TargetPort = 919 231 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID 449da2ba-9ed4-4078-b261-77946f31f3bd;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "Requirements.sbs";
						- _subsystem = "Requirements";
						- _class = "";
						- _name = "LLR Cal Max";
						- _id = GUID 3a2cf409-4d1e-4c9a-9bfb-c290a2e9caa2;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "LLR Cal Max";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 12bcbe5b-0dfe-4770-9fd0-c05505219122;
					- m_sourceType = 'F';
					- m_pTarget = GUID 9ff661d4-d8ca-48ee-aa96-4c5548b78ef8;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "derive";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  62 -9  62 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 234 873 ;
						- m_nHorizontalSpacing = -24;
						- m_nVerticalSpacing = 152;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 1 301 891  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 297 1070 ;
					- m_TargetPort = 1041 565 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID 679fb2c2-ebd6-41bd-b0a5-bb44fa1ed545;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "Requirements.sbs";
						- _subsystem = "Requirements";
						- _class = "";
						- _name = "LLR Cal Min";
						- _id = GUID 3a9bf658-245f-484d-82d1-6bcfeb633730;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "LLR Cal Min";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 12bcbe5b-0dfe-4770-9fd0-c05505219122;
					- m_sourceType = 'F';
					- m_pTarget = GUID bcda1f91-c486-407a-a4ee-10b09ba9da3a;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "derive";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  62 -9  62 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 258 1065 ;
						- m_nHorizontalSpacing = -36;
						- m_nVerticalSpacing = 245;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 1 337 1078  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 515 1034 ;
					- m_TargetPort = 1038 611 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID 4ffe1b72-486a-4d5e-9fd1-aa5a8a00b0de;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "System.sbs";
						- _subsystem = "System";
						- _class = "";
						- _name = "HLR Follow_0";
						- _id = GUID aff21686-61f6-4b5a-a50f-fd0a265db1bd;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "HLR Follow_0";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 8f24f3e5-c603-4185-be79-17655a7dd49a;
					- m_sourceType = 'F';
					- m_pTarget = GUID da6596ea-f299-42fa-844f-14a404363059;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "refine";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  59 -9  59 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 1086 249 ;
						- m_nHorizontalSpacing = 26;
						- m_nVerticalSpacing = 1;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 361 877 ;
					- m_TargetPort = 763 38 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID e041c1c0-0623-45ac-92fb-cd30172ba393;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "System.sbs";
						- _subsystem = "System";
						- _class = "";
						- _name = "HLR Untethered";
						- _id = GUID d45712af-e348-4d08-8d12-3f11c4772a68;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "HLR Untethered";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 8f24f3e5-c603-4185-be79-17655a7dd49a;
					- m_sourceType = 'F';
					- m_pTarget = GUID 8bedf126-30f1-4667-9c53-200b088882c8;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "refine";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  59 -9  59 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 942 249 ;
						- m_nHorizontalSpacing = -13;
						- m_nVerticalSpacing = 5;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 120 877 ;
					- m_TargetPort = 581 33 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID 55a8bc95-c893-4c6d-a74c-56f063b9db55;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "System.sbs";
						- _subsystem = "System";
						- _class = "";
						- _name = "HLR IR Array_0";
						- _id = GUID 17369a93-3531-42fd-853f-c930df27e00f;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "HLR IR Array_0";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 8f24f3e5-c603-4185-be79-17655a7dd49a;
					- m_sourceType = 'F';
					- m_pTarget = GUID d27813b2-f5fc-41c6-a237-c66f885c998f;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "refine";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  59 -9  59 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 1218 249 ;
						- m_nHorizontalSpacing = 59;
						- m_nVerticalSpacing = 14;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 482 877 ;
					- m_TargetPort = 799 74 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID c2fcf913-959b-4184-a8e0-7f7fb81f7821;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "System.sbs";
						- _subsystem = "System";
						- _class = "";
						- _name = "HLR Speed";
						- _id = GUID 334924c2-af40-4436-b0d6-fb86938b940c;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "HLR Speed";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 8f24f3e5-c603-4185-be79-17655a7dd49a;
					- m_sourceType = 'F';
					- m_pTarget = GUID 5b9eb42f-61b2-4772-b081-d9dd8e231fcd;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "refine";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  59 -9  59 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 1362 249 ;
						- m_nHorizontalSpacing = 4;
						- m_nVerticalSpacing = 2;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 843 877 ;
					- m_TargetPort = 578 43 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIComponent 
					- _id = GUID 2275e8ce-b447-4af0-9848-2e5b9e256310;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 145;
					- m_pModelObject = { IHandle 
						- _m2Class = "IComponent";
						- _filename = "Driver.cmp";
						- _subsystem = "";
						- _class = "";
						- _name = "Driver";
						- _id = GUID e8d2b136-7b20-43f7-91cd-12cd608855ae;
					}
					- m_pParent = GUID 46f67643-04ce-4ad1-b869-81e9432f9a65;
					- m_name = { CGIText 
						- m_str = "Driver";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 4104;
					- m_transform = 0.101523 0 0 0.0690222 1343.9 863.931 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 1 1  1 1218  1183 1218  1183 1  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				{ CGIComponent 
					- _id = GUID 16ae980e-3a43-437b-95fa-195d14a4dddf;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 145;
					- m_pModelObject = { IHandle 
						- _m2Class = "IComponent";
						- _filename = "IR_Array.cmp";
						- _subsystem = "";
						- _class = "";
						- _name = "IR_Array";
						- _id = GUID 9d7eef10-fb9b-4f5d-ad99-d6368ca646c1;
					}
					- m_pParent = GUID 46f67643-04ce-4ad1-b869-81e9432f9a65;
					- m_name = { CGIText 
						- m_str = "IR_Array";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 4104;
					- m_transform = 0.111675 0 0 0.0690222 1163.89 1043.93 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 1 1  1 1218  1183 1218  1183 1  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				{ CGIComponent 
					- _id = GUID 8a8b53e1-f706-4e93-9f8d-5aaa6830b650;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 145;
					- m_pModelObject = { IHandle 
						- _m2Class = "IComponent";
						- _filename = "Encoder_A.cmp";
						- _subsystem = "";
						- _class = "";
						- _name = "Encoder_A";
						- _id = GUID ce24be95-baea-4ba5-9cd9-9124f23a155b;
					}
					- m_pParent = GUID 46f67643-04ce-4ad1-b869-81e9432f9a65;
					- m_name = { CGIText 
						- m_str = "Encoder_A";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 4104;
					- m_transform = 0.0812183 0 0 0.0788825 1787.92 719.921 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 1 1  1 1218  1183 1218  1183 1  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				{ CGIComponent 
					- _id = GUID 790ed1c9-796b-4fcc-9bee-64646b8380ca;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 145;
					- m_pModelObject = { IHandle 
						- _m2Class = "IComponent";
						- _filename = "Encoder_B.cmp";
						- _subsystem = "";
						- _class = "";
						- _name = "Encoder_B";
						- _id = GUID 199a0090-41bd-4581-ac47-f1c6366635f8;
					}
					- m_pParent = GUID 46f67643-04ce-4ad1-b869-81e9432f9a65;
					- m_name = { CGIText 
						- m_str = "Encoder_B";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 4104;
					- m_transform = 0.0812183 0 0 0.0788825 1787.92 611.921 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 1 1  1 1218  1183 1218  1183 1  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				{ CGIInheritance 
					- _id = GUID e3e16904-07d5-4833-b334-29e3ec5dc62f;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "Requirements.sbs";
						- _subsystem = "Requirements";
						- _class = "";
						- _name = "IR_Array";
						- _id = GUID a79e37ba-29b4-4b4e-94cb-3f49ab863ab5;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "IR_Array";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 67c8cc3c-5905-4426-b2a3-e94fcaa9af98;
					- m_sourceType = 'F';
					- m_pTarget = GUID 16ae980e-3a43-437b-95fa-195d14a4dddf;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "Satisfy";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  65 -9  65 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 1158 741 ;
						- m_nHorizontalSpacing = -34;
						- m_nVerticalSpacing = 19;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 449 1094 ;
					- m_TargetPort = 538 1 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID d5aa0c8b-142b-4fe1-a027-6a3611639f71;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "Requirements.sbs";
						- _subsystem = "Requirements";
						- _class = "";
						- _name = "Driver";
						- _id = GUID 1c8db0d4-75bf-4840-aa37-b319c3ed25eb;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "Driver";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID b3cd0bd7-0aac-4e8a-af68-99e602874af1;
					- m_sourceType = 'F';
					- m_pTarget = GUID 2275e8ce-b447-4af0-9848-2e5b9e256310;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "Satisfy";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  65 -9  65 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 1338 741 ;
						- m_nHorizontalSpacing = -34;
						- m_nVerticalSpacing = 13;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 178 1013 ;
					- m_TargetPort = 710 1 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID 599b4965-ec89-410a-9d22-a933aa37abef;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "Requirements.sbs";
						- _subsystem = "Requirements";
						- _class = "";
						- _name = "Encoder_B";
						- _id = GUID 1671e07b-59d3-4b6d-b5c7-287212d4b359;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "Encoder_B";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 4d546175-a448-4398-bde5-e6e27a87f661;
					- m_sourceType = 'F';
					- m_pTarget = GUID 790ed1c9-796b-4fcc-9bee-64646b8380ca;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "Satisfy";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 987 389 ;
					- m_TargetPort = 1 914 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID f9cc6ce1-6430-4077-8fa9-65f9f93a1ed9;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "Requirements.sbs";
						- _subsystem = "Requirements";
						- _class = "";
						- _name = "Encoder_A";
						- _id = GUID 44014995-50c0-4d4a-9279-906f24f467e2;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "Encoder_A";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 4d546175-a448-4398-bde5-e6e27a87f661;
					- m_sourceType = 'F';
					- m_pTarget = GUID 8a8b53e1-f706-4e93-9f8d-5aaa6830b650;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "Satisfy";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 987 938 ;
					- m_TargetPort = 99 660 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIAnnotation 
					- _id = GUID 07c2d4d9-50a7-4515-8f24-6d779fdeade6;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 173;
					- m_pModelObject = { IHandle 
						- _m2Class = "IComment";
						- _filename = "Sources.sbs";
						- _subsystem = "Sources";
						- _class = "";
						- _name = "comment_47";
						- _id = GUID 946c92da-3b07-4bc0-bfe6-bec3ada52041;
					}
					- m_pParent = GUID 46f67643-04ce-4ad1-b869-81e9432f9a65;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.099631 0 0 0.0549451 396 131.835 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 0 3  0 1095  1084 1095  1084 3  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- _iTempdisplayTextFlag = 2;
					- m_bIsBoxStyle = 0;
				}
				{ CGIInheritance 
					- _id = GUID d48b7e9c-6c59-4f54-83fb-de837df4f8e5;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "Sources.sbs";
						- _subsystem = "Sources";
						- _class = "";
						- _name = "HLR AutoCal";
						- _id = GUID 00a749e7-4204-4d69-87e2-466faf107165;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "HLR AutoCal";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 07c2d4d9-50a7-4515-8f24-6d779fdeade6;
					- m_sourceType = 'F';
					- m_pTarget = GUID 12bcbe5b-0dfe-4770-9fd0-c05505219122;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "refine";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  59 -9  59 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 330 249 ;
						- m_nHorizontalSpacing = -35;
						- m_nVerticalSpacing = 7;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 371 895 ;
					- m_TargetPort = 679 99 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID b86ccbaa-6c67-466b-ac4b-321fd2df55b1;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "Sources.sbs";
						- _subsystem = "Sources";
						- _class = "";
						- _name = "HLR Diagnostics";
						- _id = GUID afc7ecd0-a9b6-44ee-850e-9ad14bcea31d;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "HLR Diagnostics";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 07c2d4d9-50a7-4515-8f24-6d779fdeade6;
					- m_sourceType = 'F';
					- m_pTarget = GUID 461d89a7-6d35-4cde-a3b8-b00ba530b394;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "refine";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  59 -9  59 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 522 249 ;
						- m_nHorizontalSpacing = 62;
						- m_nVerticalSpacing = 6;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 723 895 ;
					- m_TargetPort = 478 38 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIFreeText 
					- _id = GUID dc104ebe-99e3-4f06-a6b5-7cb1f820948c;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "FreeText";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "Font.Weight";
												- _Value = "700";
												- _Type = Int;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 189;
					- m_pModelObject = { IHandle 
						- _m2Class = "";
					}
					- m_pParent = GUID 46f67643-04ce-4ad1-b869-81e9432f9a65;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4096;
					- m_transform = 1 0 0 1 -36 -144 ;
					- m_bIsPreferencesInitialized = 1;
					- m_points = 4 1740 372  1781 372  1781 390  1740 390  ;
					- m_text = "High Level Requirements";
				}
				{ CGIFreeText 
					- _id = GUID 4509e112-a63d-47f8-b44d-c02ec2bc4c61;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "FreeText";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "Font.Weight";
												- _Value = "700";
												- _Type = Int;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 189;
					- m_pModelObject = { IHandle 
						- _m2Class = "";
					}
					- m_pParent = GUID 46f67643-04ce-4ad1-b869-81e9432f9a65;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4096;
					- m_transform = 1 0 0 1 24 12 ;
					- m_bIsPreferencesInitialized = 1;
					- m_points = 4 1692 540  1733 540  1733 558  1692 558  ;
					- m_text = "Low Level Requirements";
				}
				{ CGIFreeText 
					- _id = GUID e5571663-6383-40bf-b686-11bf0b2979ec;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "FreeText";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "Font.Weight";
												- _Value = "700";
												- _Type = Int;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 189;
					- m_pModelObject = { IHandle 
						- _m2Class = "";
					}
					- m_pParent = GUID 46f67643-04ce-4ad1-b869-81e9432f9a65;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4096;
					- m_transform = 1 0 0 1 -960 0 ;
					- m_bIsPreferencesInitialized = 1;
					- m_points = 4 1692 120  1733 120  1733 138  1692 138  ;
					- m_text = "Functional Requirements";
				}
				{ CGIFreeShape 
					- _id = GUID dffa3942-3cde-4079-9f82-825f59f92775;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Rectangle";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "Fill.Transparent_Fill";
												- _Value = "1";
												- _Type = Int;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 185;
					- m_pModelObject = { IHandle 
						- _m2Class = "";
					}
					- m_pParent = GUID 46f67643-04ce-4ad1-b869-81e9432f9a65;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4096;
					- m_transform = 1 0 0 0.961538 0 8.30769 ;
					- m_bIsPreferencesInitialized = 1;
					- m_points = 4 60 216  1896 216  1896 528  60 528  ;
				}
				{ CGIFreeShape 
					- _id = GUID aaf87d24-e9f0-4ef3-b2a8-c00307519a50;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Rectangle";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "Fill.Transparent_Fill";
												- _Value = "1";
												- _Type = Int;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 185;
					- m_pModelObject = { IHandle 
						- _m2Class = "";
					}
					- m_pParent = GUID 46f67643-04ce-4ad1-b869-81e9432f9a65;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_points = 4 60 540  1896 540  1896 1164  60 1164  ;
				}
				{ CGIFreeShape 
					- _id = GUID 50a7c359-90e0-4eeb-8496-b772f13564d3;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Rectangle";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "Fill.Transparent_Fill";
												- _Value = "1";
												- _Type = Int;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 185;
					- m_pModelObject = { IHandle 
						- _m2Class = "";
					}
					- m_pParent = GUID 46f67643-04ce-4ad1-b869-81e9432f9a65;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_points = 4 372 120  1320 120  1320 204  372 204  ;
				}
				
				- m_access = 'Z';
				- m_modified = 'N';
				- m_fileVersion = "";
				- m_nModifyDate = 0;
				- m_nCreateDate = 0;
				- m_creator = "";
				- m_bScaleWithZoom = 1;
				- m_arrowStyle = 'S';
				- m_pRoot = GUID 46f67643-04ce-4ad1-b869-81e9432f9a65;
				- m_currentLeftTop = 0 0 ;
				- m_currentRightBottom = 0 0 ;
			}
			- _defaultSubsystem = { IHandle 
				- _m2Class = "ISubsystem";
				- _filename = "Sources.sbs";
				- _subsystem = "";
				- _class = "";
				- _name = "Sources";
				- _id = GUID f9623802-9e64-4088-b484-572be495c316;
			}
		}
		{ IDiagram 
			- _id = GUID b02b1317-9571-48bd-9c36-d8cffd11556b;
			- _myState = 8192;
			- _properties = { IPropertyContainer 
				- Subjects = { IRPYRawContainer 
					- size = 2;
					- value = 
					{ IPropertySubject 
						- _Name = "Format";
						- Metaclasses = { IRPYRawContainer 
							- size = 3;
							- value = 
							{ IPropertyMetaclass 
								- _Name = "Comment";
								- Properties = { IRPYRawContainer 
									- size = 7;
									- value = 
									{ IProperty 
										- _Name = "DefaultSize";
										- _Value = "0,0,84,96";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Fill.FillColor";
										- _Value = "255,255,207";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "225,225,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "Depends";
								- Properties = { IRPYRawContainer 
									- size = 6;
									- value = 
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,128";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "0,16,230";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineStyle";
										- _Value = "1";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "0";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "Package";
								- Properties = { IRPYRawContainer 
									- size = 7;
									- value = 
									{ IProperty 
										- _Name = "DefaultSize";
										- _Value = "0,0,216,151";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Fill.FillColor";
										- _Value = "255,255,255";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "221,0,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
						}
					}
					{ IPropertySubject 
						- _Name = "General";
						- Metaclasses = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertyMetaclass 
								- _Name = "Graphics";
								- Properties = { IRPYRawContainer 
									- size = 2;
									- value = 
									{ IProperty 
										- _Name = "grid_display";
										- _Value = "False";
										- _Type = Bool;
									}
									{ IProperty 
										- _Name = "grid_snap";
										- _Value = "True";
										- _Type = Bool;
									}
								}
							}
						}
					}
				}
			}
			- _name = "packages";
			- _objectCreation = "59175172546201610308571159";
			- _umlDependencyID = "2535";
			- _lastModifiedTime = "11.25.2016::12:46:37";
			- _graphicChart = { CGIClassChart 
				- _id = GUID f24cd695-9d8b-41ba-a9c1-3787ad2bdbe6;
				- m_type = 0;
				- m_pModelObject = { IHandle 
					- _m2Class = "IDiagram";
					- _id = GUID b02b1317-9571-48bd-9c36-d8cffd11556b;
				}
				- m_pParent = ;
				- m_name = { CGIText 
					- m_str = "";
					- m_style = "Arial" 10 0 0 0 1 ;
					- m_color = { IColor 
						- m_fgColor = 0;
						- m_bgColor = 0;
						- m_bgFlag = 0;
					}
					- m_position = 1 0 0  ;
					- m_nIdent = 0;
					- m_bImplicitSetRectPoints = 0;
					- m_nOrientationCtrlPt = 8;
				}
				- m_drawBehavior = 0;
				- m_bIsPreferencesInitialized = 0;
				- elementList = 46;
				{ CGIClass 
					- _id = GUID 58ee39fa-3ab9-418d-aeca-c162f2be9ed2;
					- m_type = 78;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "Sources.sbs";
						- _subsystem = "Sources";
						- _class = "";
						- _name = "TopLevel";
						- _id = GUID c96d5194-58ed-4182-82e6-04845c227d30;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "TopLevel";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 0;
					- m_bIsPreferencesInitialized = 0;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 0 ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Attrs = { IRPYRawContainer 
						- size = 0;
					}
					- Operations = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIPackage 
					- _id = GUID 6ee34660-7566-4a22-a0fc-68edf87120d9;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 127;
					- m_pModelObject = { IHandle 
						- _m2Class = "ISubsystem";
						- _filename = "hal.sbs";
						- _subsystem = "Sources";
						- _class = "";
						- _name = "hal";
						- _id = GUID 9d76869b-fd0a-412e-a4db-424509c70211;
					}
					- m_pParent = GUID 58ee39fa-3ab9-418d-aeca-c162f2be9ed2;
					- m_name = { CGIText 
						- m_str = "hal";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 4104;
					- m_transform = 0.138158 0 0 0.0729799 492 456.441 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 0 0  0 1151  1216 1151  1216 0  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				{ CGIPackage 
					- _id = GUID 768d67db-76db-4451-a623-ed26d296aaba;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 127;
					- m_pModelObject = { IHandle 
						- _m2Class = "ISubsystem";
						- _filename = "main.sbs";
						- _subsystem = "Sources";
						- _class = "";
						- _name = "main";
						- _id = GUID e415ef3e-1fba-4c75-8b90-6540a18a10f4;
					}
					- m_pParent = GUID 58ee39fa-3ab9-418d-aeca-c162f2be9ed2;
					- m_name = { CGIText 
						- m_str = "main";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 4104;
					- m_transform = 0.138158 0 0 0.067767 492 324.305 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 0 0  0 1151  1216 1151  1216 0  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				{ CGIPackage 
					- _id = GUID 601a0c24-43dc-463e-b4d9-0cc9b6ba822a;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 127;
					- m_pModelObject = { IHandle 
						- _m2Class = "ISubsystem";
						- _filename = "adc.sbs";
						- _subsystem = "Sources::hal";
						- _class = "";
						- _name = "adc";
						- _id = GUID cd6597e3-99c9-442c-b253-88c58f045d8f;
					}
					- m_pParent = GUID 58ee39fa-3ab9-418d-aeca-c162f2be9ed2;
					- m_name = { CGIText 
						- m_str = "adc";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 4104;
					- m_transform = 0.137624 0 0 0.0681054 936 96 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 0 0  0 1151  1216 1151  1216 0  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				{ CGIPackage 
					- _id = GUID 14d405fa-5a21-40f3-b438-6616c646ea05;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 127;
					- m_pModelObject = { IHandle 
						- _m2Class = "ISubsystem";
						- _filename = "controller.sbs";
						- _subsystem = "Sources::hal";
						- _class = "";
						- _name = "controller";
						- _id = GUID 60410c4e-2ac1-4e32-a1e4-cad6240bf27b;
					}
					- m_pParent = GUID 58ee39fa-3ab9-418d-aeca-c162f2be9ed2;
					- m_name = { CGIText 
						- m_str = "controller";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 4104;
					- m_transform = 0.137624 0 0 0.0681054 935.74 176.957 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 0 0  0 1151  1216 1151  1216 0  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				{ CGIPackage 
					- _id = GUID d9fb2215-0cc0-422c-9bac-386ef4186726;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 127;
					- m_pModelObject = { IHandle 
						- _m2Class = "ISubsystem";
						- _filename = "diagnostics.sbs";
						- _subsystem = "Sources::hal";
						- _class = "";
						- _name = "diagnostics";
						- _id = GUID ca62b407-67ef-4809-8221-ea15f57f183e;
					}
					- m_pParent = GUID 58ee39fa-3ab9-418d-aeca-c162f2be9ed2;
					- m_name = { CGIText 
						- m_str = "diagnostics";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 4104;
					- m_transform = 0.137336 0 0 0.0677672 936 258 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 0 0  0 1151  1216 1151  1216 0  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				{ CGIPackage 
					- _id = GUID 0fb035a4-1c5a-4f85-8fc5-86877b121b82;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 127;
					- m_pModelObject = { IHandle 
						- _m2Class = "ISubsystem";
						- _filename = "driver.sbs";
						- _subsystem = "Sources::hal";
						- _class = "";
						- _name = "driver";
						- _id = GUID ada89d98-a664-4a3e-b908-a40fe4d34c30;
					}
					- m_pParent = GUID 58ee39fa-3ab9-418d-aeca-c162f2be9ed2;
					- m_name = { CGIText 
						- m_str = "driver";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 4104;
					- m_transform = 0.137336 0 0 0.0677672 936 339 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 0 0  0 1151  1216 1151  1216 0  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				{ CGIPackage 
					- _id = GUID 152aee3e-939c-4321-867d-019d6ee05b25;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 127;
					- m_pModelObject = { IHandle 
						- _m2Class = "ISubsystem";
						- _filename = "encoder.sbs";
						- _subsystem = "Sources::hal";
						- _class = "";
						- _name = "encoder";
						- _id = GUID 63d37f8e-344f-4f34-9891-a642f221ada0;
					}
					- m_pParent = GUID 58ee39fa-3ab9-418d-aeca-c162f2be9ed2;
					- m_name = { CGIText 
						- m_str = "encoder";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 4104;
					- m_transform = 0.137624 0 0 0.0681054 935.96 419.827 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 0 0  0 1151  1216 1151  1216 0  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				{ CGIPackage 
					- _id = GUID 8cb1eeb0-b16e-43f2-affa-14fe8ed05bfc;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 127;
					- m_pModelObject = { IHandle 
						- _m2Class = "ISubsystem";
						- _filename = "hmi.sbs";
						- _subsystem = "Sources::hal";
						- _class = "";
						- _name = "hmi";
						- _id = GUID 7290b49b-2bd4-427f-a6a0-6898e7ec8a20;
					}
					- m_pParent = GUID 58ee39fa-3ab9-418d-aeca-c162f2be9ed2;
					- m_name = { CGIText 
						- m_str = "hmi";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 4104;
					- m_transform = 0.137624 0 0 0.0681054 935.69 500.784 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 0 0  0 1151  1216 1151  1216 0  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				{ CGIPackage 
					- _id = GUID 071a40f5-c416-4532-a729-dac71fecf028;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 127;
					- m_pModelObject = { IHandle 
						- _m2Class = "ISubsystem";
						- _filename = "mcg.sbs";
						- _subsystem = "Sources::hal";
						- _class = "";
						- _name = "mcg";
						- _id = GUID 0a54d37b-facf-4ff5-b353-bbe3e6d15b0d;
					}
					- m_pParent = GUID 58ee39fa-3ab9-418d-aeca-c162f2be9ed2;
					- m_name = { CGIText 
						- m_str = "mcg";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 4104;
					- m_transform = 0.137336 0 0 0.0677672 936 582 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 0 0  0 1151  1216 1151  1216 0  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				{ CGIPackage 
					- _id = GUID a78ccd44-68b5-4078-a3d6-85bf8e5c6cf8;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 127;
					- m_pModelObject = { IHandle 
						- _m2Class = "ISubsystem";
						- _filename = "target_definitions.sbs";
						- _subsystem = "Sources::hal";
						- _class = "";
						- _name = "target_definitions";
						- _id = GUID 19f85f0f-5922-4e4a-8ee2-63d4eb7e14eb;
					}
					- m_pParent = GUID 58ee39fa-3ab9-418d-aeca-c162f2be9ed2;
					- m_name = { CGIText 
						- m_str = "target_definitions";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 4104;
					- m_transform = 0.137336 0 0 0.0677672 936 663 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 0 0  0 1151  1216 1151  1216 0  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				{ CGIPackage 
					- _id = GUID daaf3604-8346-4e64-be05-22fefffcae5e;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 127;
					- m_pModelObject = { IHandle 
						- _m2Class = "ISubsystem";
						- _filename = "uart.sbs";
						- _subsystem = "Sources::hal";
						- _class = "";
						- _name = "uart";
						- _id = GUID 2fe8a6c2-bb4d-414f-8fa3-164702cc22a7;
					}
					- m_pParent = GUID 58ee39fa-3ab9-418d-aeca-c162f2be9ed2;
					- m_name = { CGIText 
						- m_str = "uart";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 4104;
					- m_transform = 0.137624 0 0 0.0681054 935.91 743.654 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 0 0  0 1151  1216 1151  1216 0  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				{ CGIPackage 
					- _id = GUID 26590448-49f5-41da-b070-abe0436942ef;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 127;
					- m_pModelObject = { IHandle 
						- _m2Class = "ISubsystem";
						- _filename = "util.sbs";
						- _subsystem = "Sources::hal";
						- _class = "";
						- _name = "util";
						- _id = GUID 90a34774-303e-417c-99b9-4fd3fc96a8b0;
					}
					- m_pParent = GUID 58ee39fa-3ab9-418d-aeca-c162f2be9ed2;
					- m_name = { CGIText 
						- m_str = "util";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 4104;
					- m_transform = 0.137624 0 0 0.0681054 935.65 824.611 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 0 0  0 1151  1216 1151  1216 0  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				{ CGIPackage 
					- _id = GUID ebc4d6ef-c68a-49f5-919e-6895c032a750;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 127;
					- m_pModelObject = { IHandle 
						- _m2Class = "ISubsystem";
						- _filename = "Sources.sbs";
						- _subsystem = "";
						- _class = "";
						- _name = "Sources";
						- _id = GUID f9623802-9e64-4088-b484-572be495c316;
					}
					- m_pParent = GUID 58ee39fa-3ab9-418d-aeca-c162f2be9ed2;
					- m_name = { CGIText 
						- m_str = "Sources";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 4104;
					- m_transform = 0.138158 0 0 0.0677672 132 444 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 0 0  0 1151  1216 1151  1216 0  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				{ CGIPackage 
					- _id = GUID db9b07b7-d38e-4f4b-9e2b-1cbabb0178be;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 127;
					- m_pModelObject = { IHandle 
						- _m2Class = "ISubsystem";
						- _filename = "System.sbs";
						- _subsystem = "";
						- _class = "";
						- _name = "System";
						- _id = GUID 07685dbe-5566-4a67-8dda-a128e6d2b138;
					}
					- m_pParent = GUID 58ee39fa-3ab9-418d-aeca-c162f2be9ed2;
					- m_name = { CGIText 
						- m_str = "System";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 4104;
					- m_transform = 0.138158 0 0 0.0677672 132 144 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 0 0  0 1151  1216 1151  1216 0  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				{ CGIInheritance 
					- _id = GUID 52fdc2e5-5e79-47e7-803e-9bdd1ff3f017;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "hal.sbs";
						- _subsystem = "Sources::hal";
						- _class = "";
						- _name = "adc";
						- _id = GUID c52126b8-6259-47c1-b83b-b1287fe571db;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "adc";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 6ee34660-7566-4a22-a0fc-68edf87120d9;
					- m_sourceType = 'F';
					- m_pTarget = GUID 601a0c24-43dc-463e-b4d9-0cc9b6ba822a;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "subfolder";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  70 -9  70 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 870 141 ;
						- m_nHorizontalSpacing = 53;
						- m_nVerticalSpacing = -278;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 2 864 504  864 135  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 1216 652 ;
					- m_TargetPort = 0 573 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID 0fda54c9-f12a-4d9d-a82e-1386902b9d36;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "hal.sbs";
						- _subsystem = "Sources::hal";
						- _class = "";
						- _name = "controller";
						- _id = GUID fcf4ff7e-3d99-4d4b-b5f6-acf42c52d17d;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "controller";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 6ee34660-7566-4a22-a0fc-68edf87120d9;
					- m_sourceType = 'F';
					- m_pTarget = GUID 14d405fa-5a21-40f3-b438-6616c646ea05;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "subfolder";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  70 -9  70 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 870 225 ;
						- m_nHorizontalSpacing = 53;
						- m_nVerticalSpacing = -230;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 2 864 504  864 216  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 1216 652 ;
					- m_TargetPort = 176 573 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID 0e4bfe06-6016-4e07-966f-6860f20a8657;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "hal.sbs";
						- _subsystem = "Sources::hal";
						- _class = "";
						- _name = "diagnostics";
						- _id = GUID 581c4079-62c9-4a8f-b470-f04a927e3595;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "diagnostics";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 6ee34660-7566-4a22-a0fc-68edf87120d9;
					- m_sourceType = 'F';
					- m_pTarget = GUID d9fb2215-0cc0-422c-9bac-386ef4186726;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "subfolder";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  70 -9  70 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 870 309 ;
						- m_nHorizontalSpacing = 53;
						- m_nVerticalSpacing = -183;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 2 864 504  864 300  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 1216 652 ;
					- m_TargetPort = 87 620 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID 2565f7fe-e228-4400-8d7b-8440505b95bd;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "hal.sbs";
						- _subsystem = "Sources::hal";
						- _class = "";
						- _name = "driver";
						- _id = GUID acab05c3-44ba-40c2-8322-20826f17a05f;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "driver";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 6ee34660-7566-4a22-a0fc-68edf87120d9;
					- m_sourceType = 'F';
					- m_pTarget = GUID 0fb035a4-1c5a-4f85-8fc5-86877b121b82;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "subfolder";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  70 -9  70 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 870 381 ;
						- m_nHorizontalSpacing = 60;
						- m_nVerticalSpacing = -138;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 2 864 504  864 375  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 1216 665 ;
					- m_TargetPort = 87 531 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID b139c229-c651-437f-976b-ebbc9a7cd51a;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "hal.sbs";
						- _subsystem = "Sources::hal";
						- _class = "";
						- _name = "encoder";
						- _id = GUID 2a9147f1-66f4-47bb-8f48-b18485a91eca;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "encoder";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 6ee34660-7566-4a22-a0fc-68edf87120d9;
					- m_sourceType = 'F';
					- m_pTarget = GUID 152aee3e-939c-4321-867d-019d6ee05b25;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "subfolder";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  70 -9  70 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 870 465 ;
						- m_nHorizontalSpacing = 97;
						- m_nVerticalSpacing = -54;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 2 864 504  864 459  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 1216 665 ;
					- m_TargetPort = 87 575 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID 75735274-0937-4429-9cd2-95a5e16ef92e;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "hal.sbs";
						- _subsystem = "Sources::hal";
						- _class = "";
						- _name = "hmi";
						- _id = GUID 73019743-c5af-4156-ab9f-269c5450bae4;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "hmi";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 6ee34660-7566-4a22-a0fc-68edf87120d9;
					- m_sourceType = 'F';
					- m_pTarget = GUID 8cb1eeb0-b16e-43f2-affa-14fe8ed05bfc;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "subfolder";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  70 -9  70 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 870 549 ;
						- m_nHorizontalSpacing = 99;
						- m_nVerticalSpacing = 30;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 2 864 504  864 543  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 1216 652 ;
					- m_TargetPort = 89 620 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID dcf7a647-3150-4605-9949-465021adaeae;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "hal.sbs";
						- _subsystem = "Sources::hal";
						- _class = "";
						- _name = "mcg";
						- _id = GUID 633030f0-4194-4197-a68d-1af5222cf5c1;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "mcg";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 6ee34660-7566-4a22-a0fc-68edf87120d9;
					- m_sourceType = 'F';
					- m_pTarget = GUID 071a40f5-c416-4532-a729-dac71fecf028;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "subfolder";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  70 -9  70 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 870 633 ;
						- m_nHorizontalSpacing = 65;
						- m_nVerticalSpacing = 114;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 2 864 504  864 622  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 1216 652 ;
					- m_TargetPort = 87 590 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID 39bb4c39-3c33-49a1-b661-8a04b69677f2;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "hal.sbs";
						- _subsystem = "Sources::hal";
						- _class = "";
						- _name = "target_definitions";
						- _id = GUID 0d1d77ba-46fd-4c38-8372-bf703ad51510;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "target_definitions";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 6ee34660-7566-4a22-a0fc-68edf87120d9;
					- m_sourceType = 'F';
					- m_pTarget = GUID a78ccd44-68b5-4078-a3d6-85bf8e5c6cf8;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "subfolder";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  70 -9  70 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 870 705 ;
						- m_nHorizontalSpacing = 53;
						- m_nVerticalSpacing = 193;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 2 864 504  864 699  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 1216 652 ;
					- m_TargetPort = 175 531 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID b0da17a0-fe6f-4673-8028-d0d3714ee710;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "hal.sbs";
						- _subsystem = "Sources::hal";
						- _class = "";
						- _name = "uart";
						- _id = GUID b8d1f223-8d67-4a26-892d-d6e3b7ea6cba;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "uart";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 6ee34660-7566-4a22-a0fc-68edf87120d9;
					- m_sourceType = 'F';
					- m_pTarget = GUID daaf3604-8346-4e64-be05-22fefffcae5e;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "subfolder";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  70 -9  70 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 870 789 ;
						- m_nHorizontalSpacing = 53;
						- m_nVerticalSpacing = 241;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 2 864 504  864 781  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 1216 652 ;
					- m_TargetPort = 1 548 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID 8e5e5ba2-b151-46bd-88db-7ac01f09e41b;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "hal.sbs";
						- _subsystem = "Sources::hal";
						- _class = "";
						- _name = "util";
						- _id = GUID 943f25bc-882b-4f35-8dba-e0a0901c6f58;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "util";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 6ee34660-7566-4a22-a0fc-68edf87120d9;
					- m_sourceType = 'F';
					- m_pTarget = GUID 26590448-49f5-41da-b070-abe0436942ef;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "subfolder";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  70 -9  70 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 870 873 ;
						- m_nHorizontalSpacing = 53;
						- m_nVerticalSpacing = 286;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 2 864 504  864 865  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 1216 652 ;
					- m_TargetPort = 90 593 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID d74cf41c-f3a1-4ca3-b579-0238accc233a;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "main.sbs";
						- _subsystem = "Sources::main";
						- _class = "";
						- _name = "hal";
						- _id = GUID 62e54dcf-eb50-4f2c-9758-156704bf89ef;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "hal";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 768d67db-76db-4451-a623-ed26d296aaba;
					- m_sourceType = 'F';
					- m_pTarget = GUID 6ee34660-7566-4a22-a0fc-68edf87120d9;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "include";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  70 -9  70 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 558 429 ;
						- m_nHorizontalSpacing = -19;
						- m_nVerticalSpacing = -8;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 955 1058 ;
					- m_TargetPort = 955 487 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID f1cd8305-c2f3-4369-a35d-62ceb73be117;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "adc.sbs";
						- _subsystem = "Sources::hal::adc";
						- _class = "";
						- _name = "System";
						- _id = GUID 51de729b-aad1-412b-8b5c-8850aca903a8;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "System";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 601a0c24-43dc-463e-b4d9-0cc9b6ba822a;
					- m_sourceType = 'F';
					- m_pTarget = GUID db9b07b7-d38e-4f4b-9e2b-1cbabb0178be;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "include";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  70 -9  70 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 786 165 ;
						- m_nHorizontalSpacing = 144;
						- m_nVerticalSpacing = -54;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 2 780 156  780 204  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 0 881 ;
					- m_TargetPort = 1042 885 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID 48ea7bd1-d51c-4c29-8551-ff51108adc61;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "controller.sbs";
						- _subsystem = "Sources::hal::controller";
						- _class = "";
						- _name = "System";
						- _id = GUID 94cd9042-47bf-4bff-8d95-ee9dd9c321b0;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "System";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 14d405fa-5a21-40f3-b438-6616c646ea05;
					- m_sourceType = 'F';
					- m_pTarget = GUID db9b07b7-d38e-4f4b-9e2b-1cbabb0178be;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "include";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  70 -9  70 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 786 249 ;
						- m_nHorizontalSpacing = 148;
						- m_nVerticalSpacing = 30;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 2 780 240  780 204  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 89 926 ;
					- m_TargetPort = 1129 885 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID 486ec550-06ee-436b-885e-485e59d65249;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "diagnostics.sbs";
						- _subsystem = "Sources::hal::diagnostics";
						- _class = "";
						- _name = "System";
						- _id = GUID 26751876-e6a9-476f-b862-e386087f9a42;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "System";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID d9fb2215-0cc0-422c-9bac-386ef4186726;
					- m_sourceType = 'F';
					- m_pTarget = GUID db9b07b7-d38e-4f4b-9e2b-1cbabb0178be;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "include";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  70 -9  70 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 786 333 ;
						- m_nHorizontalSpacing = 105;
						- m_nVerticalSpacing = 114;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 2 780 324  780 204  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 0 974 ;
					- m_TargetPort = 1042 885 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID e7cf9dd6-1060-4810-bff4-5f5f18162f30;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "driver.sbs";
						- _subsystem = "Sources::hal::driver";
						- _class = "";
						- _name = "System";
						- _id = GUID 873e8b4c-c645-49b5-93b1-ed51247256b4;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "System";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 0fb035a4-1c5a-4f85-8fc5-86877b121b82;
					- m_sourceType = 'F';
					- m_pTarget = GUID db9b07b7-d38e-4f4b-9e2b-1cbabb0178be;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "include";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  70 -9  70 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 786 405 ;
						- m_nHorizontalSpacing = 62;
						- m_nVerticalSpacing = 186;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 2 780 396  780 204  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 87 841 ;
					- m_TargetPort = 1129 885 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID 0c18ac6c-ea16-4201-846e-e7fe07e22fb2;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "encoder.sbs";
						- _subsystem = "Sources::hal::encoder";
						- _class = "";
						- _name = "System";
						- _id = GUID fc149ac4-09d7-4e30-bef7-fe7bebee4d54;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "System";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 152aee3e-939c-4321-867d-019d6ee05b25;
					- m_sourceType = 'F';
					- m_pTarget = GUID db9b07b7-d38e-4f4b-9e2b-1cbabb0178be;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "include";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  70 -9  70 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 786 489 ;
						- m_nHorizontalSpacing = 53;
						- m_nVerticalSpacing = 263;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 2 780 480  780 204  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 87 884 ;
					- m_TargetPort = 1129 885 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID 04545f57-39e8-42c2-ae89-7abb0f73e3e4;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "hmi.sbs";
						- _subsystem = "Sources::hal::hmi";
						- _class = "";
						- _name = "System";
						- _id = GUID 734e53bb-e924-4d88-9b9c-4aec53a1aef1;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "System";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 8cb1eeb0-b16e-43f2-affa-14fe8ed05bfc;
					- m_sourceType = 'F';
					- m_pTarget = GUID db9b07b7-d38e-4f4b-9e2b-1cbabb0178be;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "include";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  70 -9  70 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 786 573 ;
						- m_nHorizontalSpacing = 53;
						- m_nVerticalSpacing = 301;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 2 780 564  780 204  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 2 928 ;
					- m_TargetPort = 695 885 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID a5e43640-0042-4e95-b12c-f448c7c8f648;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "mcg.sbs";
						- _subsystem = "Sources::hal::mcg";
						- _class = "";
						- _name = "System";
						- _id = GUID 24db531a-1632-42dc-a9e4-230088ff95f8;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "System";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 071a40f5-c416-4532-a729-dac71fecf028;
					- m_sourceType = 'F';
					- m_pTarget = GUID db9b07b7-d38e-4f4b-9e2b-1cbabb0178be;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "include";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  70 -9  70 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 786 657 ;
						- m_nHorizontalSpacing = 53;
						- m_nVerticalSpacing = 338;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 2 780 646  780 204  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 87 944 ;
					- m_TargetPort = 1042 885 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID b4d89188-d487-49fa-8289-55c6b07b6b63;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "target_definitions.sbs";
						- _subsystem = "Sources::hal::target_definitions";
						- _class = "";
						- _name = "System";
						- _id = GUID 47a02aca-005d-418d-ab47-5b3a6558c9b4;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "System";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID a78ccd44-68b5-4078-a3d6-85bf8e5c6cf8;
					- m_sourceType = 'F';
					- m_pTarget = GUID db9b07b7-d38e-4f4b-9e2b-1cbabb0178be;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "include";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  70 -9  70 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 786 741 ;
						- m_nHorizontalSpacing = 53;
						- m_nVerticalSpacing = 379;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 2 780 732  780 204  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 0 1018 ;
					- m_TargetPort = 1216 885 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID 9d53053f-c5ce-46d3-a2a2-19159ad88fd7;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "uart.sbs";
						- _subsystem = "Sources::hal::uart";
						- _class = "";
						- _name = "System";
						- _id = GUID 8afc099e-9741-4d5c-bf69-47ad64f1da32;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "System";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID daaf3604-8346-4e64-be05-22fefffcae5e;
					- m_sourceType = 'F';
					- m_pTarget = GUID db9b07b7-d38e-4f4b-9e2b-1cbabb0178be;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "include";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  70 -9  70 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 786 813 ;
						- m_nHorizontalSpacing = 53;
						- m_nVerticalSpacing = 411;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 2 780 804  780 204  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 88 886 ;
					- m_TargetPort = 1129 885 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID 433c24a9-56ff-41dd-8d54-481bdd6d69a8;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "util.sbs";
						- _subsystem = "Sources::hal::util";
						- _class = "";
						- _name = "System";
						- _id = GUID 66bdc5b7-d81c-4d2a-b19b-9097111ed03e;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "System";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 26590448-49f5-41da-b070-abe0436942ef;
					- m_sourceType = 'F';
					- m_pTarget = GUID db9b07b7-d38e-4f4b-9e2b-1cbabb0178be;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "include";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  70 -9  70 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 786 897 ;
						- m_nHorizontalSpacing = 53;
						- m_nVerticalSpacing = 447;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 2 780 888  780 204  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 90 931 ;
					- m_TargetPort = 1129 885 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID b4cfc5a1-cd97-4ab6-804b-91937f68cca5;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "Sources.sbs";
						- _subsystem = "Sources";
						- _class = "";
						- _name = "hal";
						- _id = GUID bf399717-a938-41f9-8119-2408fca5208e;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "hal";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID ebc4d6ef-c68a-49f5-919e-6895c032a750;
					- m_sourceType = 'F';
					- m_pTarget = GUID 6ee34660-7566-4a22-a0fc-68edf87120d9;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "subfolder";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  81 -9  81 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 330 441 ;
						- m_nHorizontalSpacing = -19;
						- m_nVerticalSpacing = -6;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 1216 885 ;
					- m_TargetPort = 0 652 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIAnnotation 
					- _id = GUID ba5d32ad-4d15-4281-912a-f0bf02cc332d;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Comment";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "Font.Weight";
												- _Value = "400";
												- _Type = Int;
											}
										}
									}
								}
							}
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 173;
					- m_pModelObject = { IHandle 
						- _m2Class = "IComment";
						- _filename = "Sources.sbs";
						- _subsystem = "Sources";
						- _class = "";
						- _name = "comment_43";
						- _id = GUID 375eb614-8a2b-49f4-8f9a-56f7afbb2874;
					}
					- m_pParent = GUID 58ee39fa-3ab9-418d-aeca-c162f2be9ed2;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.265683 0 0 0.0769231 132 659.769 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 0 3  0 1095  1084 1095  1084 3  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- _iTempdisplayTextFlag = 2;
					- m_bIsBoxStyle = 0;
				}
				{ CGIAnnotation 
					- _id = GUID df94e5ab-9951-42de-9538-c92f738a653d;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 173;
					- m_pModelObject = { IHandle 
						- _m2Class = "IComment";
						- _filename = "Sources.sbs";
						- _subsystem = "Sources";
						- _class = "";
						- _name = "comment_44";
						- _id = GUID 80df0e9d-5e18-4c3f-8cea-b58b535c41c3;
					}
					- m_pParent = GUID 58ee39fa-3ab9-418d-aeca-c162f2be9ed2;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.387454 0 0 0.0879121 96 11.7363 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 0 3  0 1095  1084 1095  1084 3  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- _iTempdisplayTextFlag = 2;
					- m_bIsBoxStyle = 0;
				}
				{ CGIInheritance 
					- _id = GUID 2fb72987-d5ed-4572-a4cc-6d3a40a5fc53;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "Sources.sbs";
						- _subsystem = "Sources";
						- _class = "";
						- _name = "main";
						- _id = GUID 4d3c21a6-4cb4-4b28-b123-885997272348;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "main";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID ebc4d6ef-c68a-49f5-919e-6895c032a750;
					- m_sourceType = 'F';
					- m_pTarget = GUID 768d67db-76db-4451-a623-ed26d296aaba;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "subfolder";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  81 -9  81 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 330 489 ;
						- m_nHorizontalSpacing = -26;
						- m_nVerticalSpacing = 38;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 2 408 478  408 372  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 1216 502 ;
					- m_TargetPort = 261 704 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIPackage 
					- _id = GUID a6c75f84-1309-4a4d-b5c5-7902bba018db;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 127;
					- m_pModelObject = { IHandle 
						- _m2Class = "ISubsystem";
						- _filename = "ir_array.sbs";
						- _subsystem = "Sources::hal";
						- _class = "";
						- _name = "ir_array";
						- _id = GUID 0d42f7ce-ee80-4a51-8ef9-ed8bd9979e65;
					}
					- m_pParent = GUID 58ee39fa-3ab9-418d-aeca-c162f2be9ed2;
					- m_name = { CGIText 
						- m_str = "ir_array";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 4104;
					- m_transform = 0.138158 0 0 0.07298 936 912.205 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 0 0  0 1151  1216 1151  1216 0  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				{ CGIInheritance 
					- _id = GUID e374f7d9-f392-41c0-a2dc-f01055753cea;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "hal.sbs";
						- _subsystem = "Sources::hal";
						- _class = "";
						- _name = "ir_array";
						- _id = GUID 061ae579-9fae-4c10-a6b2-c4fc7d152382;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "ir_array";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 6ee34660-7566-4a22-a0fc-68edf87120d9;
					- m_sourceType = 'F';
					- m_pTarget = GUID a6c75f84-1309-4a4d-b5c5-7902bba018db;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "subfolder";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  81 -9  81 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 858 981 ;
						- m_nHorizontalSpacing = 46;
						- m_nVerticalSpacing = 345;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 2 864 504  864 973  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 1173 652 ;
					- m_TargetPort = 58 833 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID 9d19bc43-714c-4d3c-a293-91e7a2c9bb01;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "ir_array.sbs";
						- _subsystem = "Sources::hal::ir_array";
						- _class = "";
						- _name = "System";
						- _id = GUID 3d0d49ac-eda9-4bdf-9b35-b277d5184bc9;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "System";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID a6c75f84-1309-4a4d-b5c5-7902bba018db;
					- m_sourceType = 'F';
					- m_pTarget = GUID db9b07b7-d38e-4f4b-9e2b-1cbabb0178be;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "include";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  70 -9  70 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 786 957 ;
						- m_nHorizontalSpacing = 53;
						- m_nVerticalSpacing = 478;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 2 780 948  780 204  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 87 490 ;
					- m_TargetPort = 1209 885 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIPackage 
					- _id = GUID 3920610f-ed0b-40fa-aefa-0ce113157bb0;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 127;
					- m_pModelObject = { IHandle 
						- _m2Class = "ISubsystem";
						- _filename = "vsense.sbs";
						- _subsystem = "Sources::hal";
						- _class = "";
						- _name = "vsense";
						- _id = GUID e1623d8f-0139-4eff-98ab-ee8527fa7cad;
					}
					- m_pParent = GUID 58ee39fa-3ab9-418d-aeca-c162f2be9ed2;
					- m_name = { CGIText 
						- m_str = "vsense";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 4104;
					- m_transform = 0.138158 0 0 0.0807993 936 1009.23 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 0 0  0 1151  1216 1151  1216 0  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				{ CGIInheritance 
					- _id = GUID 0410c011-2855-4385-9f11-8ea2fb3a8e5f;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "hal.sbs";
						- _subsystem = "Sources::hal";
						- _class = "";
						- _name = "vsense";
						- _id = GUID 52aaafe1-ee46-443d-ad43-60e8820dea18;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "vsense";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 6ee34660-7566-4a22-a0fc-68edf87120d9;
					- m_sourceType = 'F';
					- m_pTarget = GUID 3920610f-ed0b-40fa-aefa-0ce113157bb0;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "subfolder";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  81 -9  81 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 858 1101 ;
						- m_nHorizontalSpacing = 45;
						- m_nVerticalSpacing = 415;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 2 864 504  864 1091  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 1216 652 ;
					- m_TargetPort = 36 1012 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID cc3d5742-b339-4823-91b1-6cc120b27a7a;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "vsense.sbs";
						- _subsystem = "Sources::hal::vsense";
						- _class = "";
						- _name = "System";
						- _id = GUID a0c9be99-e86b-4b1d-9230-76c5d3ed7ddd;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "System";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 3920610f-ed0b-40fa-aefa-0ce113157bb0;
					- m_sourceType = 'F';
					- m_pTarget = GUID db9b07b7-d38e-4f4b-9e2b-1cbabb0178be;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "include";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  70 -9  70 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 786 1053 ;
						- m_nHorizontalSpacing = 53;
						- m_nVerticalSpacing = 513;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 2 780 1044  780 204  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 0 430 ;
					- m_TargetPort = 1187 885 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				
				- m_access = 'Z';
				- m_modified = 'N';
				- m_fileVersion = "";
				- m_nModifyDate = 0;
				- m_nCreateDate = 0;
				- m_creator = "";
				- m_bScaleWithZoom = 1;
				- m_arrowStyle = 'S';
				- m_pRoot = GUID 58ee39fa-3ab9-418d-aeca-c162f2be9ed2;
				- m_currentLeftTop = 0 0 ;
				- m_currentRightBottom = 0 0 ;
			}
			- _defaultSubsystem = { IHandle 
				- _m2Class = "ISubsystem";
				- _filename = "Sources.sbs";
				- _subsystem = "";
				- _class = "";
				- _name = "Sources";
				- _id = GUID f9623802-9e64-4088-b484-572be495c316;
			}
		}
		{ IDiagram 
			- _id = GUID c5cba17d-6b70-4c4b-b55a-d0f042dabcbd;
			- _myState = 8192;
			- _properties = { IPropertyContainer 
				- Subjects = { IRPYRawContainer 
					- size = 2;
					- value = 
					{ IPropertySubject 
						- _Name = "Format";
						- Metaclasses = { IRPYRawContainer 
							- size = 5;
							- value = 
							{ IPropertyMetaclass 
								- _Name = "Association";
								- Properties = { IRPYRawContainer 
									- size = 5;
									- value = 
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,128";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "221,0,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "Class";
								- Properties = { IRPYRawContainer 
									- size = 8;
									- value = 
									{ IProperty 
										- _Name = "DefaultSize";
										- _Value = "0,34,84,148";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Fill.FillColor";
										- _Value = "255,255,255";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "121,122,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineStyle";
										- _Value = "0";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "Comment";
								- Properties = { IRPYRawContainer 
									- size = 7;
									- value = 
									{ IProperty 
										- _Name = "DefaultSize";
										- _Value = "0,0,84,96";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Fill.FillColor";
										- _Value = "255,255,207";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "225,225,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "Depends";
								- Properties = { IRPYRawContainer 
									- size = 6;
									- value = 
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,128";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "0,16,230";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineStyle";
										- _Value = "1";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "0";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "Inheritance";
								- Properties = { IRPYRawContainer 
									- size = 5;
									- value = 
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,128";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "0,16,230";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
						}
					}
					{ IPropertySubject 
						- _Name = "General";
						- Metaclasses = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertyMetaclass 
								- _Name = "Graphics";
								- Properties = { IRPYRawContainer 
									- size = 2;
									- value = 
									{ IProperty 
										- _Name = "grid_display";
										- _Value = "False";
										- _Type = Bool;
									}
									{ IProperty 
										- _Name = "grid_snap";
										- _Value = "False";
										- _Type = Bool;
									}
								}
							}
						}
					}
				}
			}
			- _name = "definition";
			- _objectCreation = "59175192546201610308551159";
			- _umlDependencyID = "2769";
			- Stereotypes = { IRPYRawContainer 
				- size = 1;
				- value = 
				{ IHandle 
					- _m2Class = "IStereotype";
					- _filename = "Sources.sbs";
					- _subsystem = "Sources";
					- _class = "";
					- _name = "stereotype_48";
					- _id = GUID 0a977eba-eb27-4b00-b55e-293fb7574be1;
				}
			}
			- _lastModifiedTime = "11.19.2016::20:7:36";
			- _graphicChart = { CGIClassChart 
				- _id = GUID 5fba9a0b-8c32-48fd-9714-e70d7196aaf8;
				- m_type = 0;
				- m_pModelObject = { IHandle 
					- _m2Class = "IDiagram";
					- _id = GUID c5cba17d-6b70-4c4b-b55a-d0f042dabcbd;
				}
				- m_pParent = ;
				- m_name = { CGIText 
					- m_str = "";
					- m_style = "Arial" 10 0 0 0 1 ;
					- m_color = { IColor 
						- m_fgColor = 0;
						- m_bgColor = 0;
						- m_bgFlag = 0;
					}
					- m_position = 1 0 0  ;
					- m_nIdent = 0;
					- m_bImplicitSetRectPoints = 0;
					- m_nOrientationCtrlPt = 8;
				}
				- m_drawBehavior = 0;
				- m_bIsPreferencesInitialized = 0;
				- elementList = 72;
				{ CGIClass 
					- _id = GUID 30b86204-7654-490a-aee3-e3c056b75669;
					- m_type = 78;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "Sources.sbs";
						- _subsystem = "Sources";
						- _class = "";
						- _name = "TopLevel";
						- _id = GUID c96d5194-58ed-4182-82e6-04845c227d30;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "TopLevel";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 0;
					- m_bIsPreferencesInitialized = 0;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 0 ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Attrs = { IRPYRawContainer 
						- size = 0;
					}
					- Operations = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIClass 
					- _id = GUID dd0eb614-2c3f-424d-a65a-4b8096cb6e08;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Class";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "Font.Size";
												- _Value = "8";
												- _Type = Int;
											}
										}
									}
								}
							}
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 87;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "System.sbs";
						- _subsystem = "System";
						- _class = "";
						- _name = "fsl_clock_manager";
						- _id = GUID 58090143-5a83-4809-abae-5608544945c1;
					}
					- m_pParent = GUID 30b86204-7654-490a-aee3-e3c056b75669;
					- m_name = { CGIText 
						- m_str = "System::fsl_clock_manager";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.135722 0 0 0.056263 559.729 413.49 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 2 329  2 1451  1061 1451  1061 329  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=50%,50%>
<frame name=AttributeListCompartment>
<frame name=PrimitiveOperationListCompartment>";
					- Attrs = { IRPYRawContainer 
						- size = 0;
					}
					- Operations = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIClass 
					- _id = GUID dd4802ab-723e-44db-882d-f8bb461ca68b;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Class";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "Font.Size";
												- _Value = "8";
												- _Type = Int;
											}
										}
									}
								}
							}
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 87;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "System.sbs";
						- _subsystem = "System";
						- _class = "";
						- _name = "fsl_debug_console";
						- _id = GUID 29c28b8b-d8c5-426b-9f55-c3cf2b8c426d;
					}
					- m_pParent = GUID 30b86204-7654-490a-aee3-e3c056b75669;
					- m_name = { CGIText 
						- m_str = "System::fsl_debug_console";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.135722 0 0 0.056263 955.593 413.177 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 2 329  2 1451  1061 1451  1061 329  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=50%,50%>
<frame name=AttributeListCompartment>
<frame name=PrimitiveOperationListCompartment>";
					- Attrs = { IRPYRawContainer 
						- size = 0;
					}
					- Operations = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIClass 
					- _id = GUID df11025c-efd4-4b69-ad4e-10beeddee420;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Class";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "Font.Size";
												- _Value = "8";
												- _Type = Int;
											}
										}
									}
								}
							}
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 87;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "System.sbs";
						- _subsystem = "System";
						- _class = "";
						- _name = "fsl_gpio_hal";
						- _id = GUID a380aea9-68fe-44b7-81db-8421b98970eb;
					}
					- m_pParent = GUID 30b86204-7654-490a-aee3-e3c056b75669;
					- m_name = { CGIText 
						- m_str = "System::fsl_gpio_hal";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.102535 0 0 0.056263 1111.47 413.864 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_bFramesetModified = 1;
					- m_polygon = 4 2 329  2 1451  1061 1451  1061 329  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=48%,52%>
<frame name=AttributeListCompartment>
<frame name=PrimitiveOperationListCompartment>";
					- Attrs = { IRPYRawContainer 
						- size = 0;
					}
					- Operations = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIClass 
					- _id = GUID cd04511f-e42f-4bc5-976b-9365a957c539;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Class";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "Font.Size";
												- _Value = "8";
												- _Type = Int;
											}
										}
									}
								}
							}
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 87;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "System.sbs";
						- _subsystem = "System";
						- _class = "";
						- _name = "fsl_interrupt_manager";
						- _id = GUID e24ba41a-3661-460f-ad79-509bcac7340a;
					}
					- m_pParent = GUID 30b86204-7654-490a-aee3-e3c056b75669;
					- m_name = { CGIText 
						- m_str = "System::fsl_interrupt_manager";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.147981 0 0 0.056263 1231.22 413.551 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 2 329  2 1451  1061 1451  1061 329  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=50%,50%>
<frame name=AttributeListCompartment>
<frame name=PrimitiveOperationListCompartment>";
					- Attrs = { IRPYRawContainer 
						- size = 0;
					}
					- Operations = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIClass 
					- _id = GUID 385df45c-8033-460a-b462-ac66640798cd;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Class";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "Font.Size";
												- _Value = "8";
												- _Type = Int;
											}
										}
									}
								}
							}
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 87;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "System.sbs";
						- _subsystem = "System";
						- _class = "";
						- _name = "fsl_port_hal";
						- _id = GUID a9fbba22-ff3c-4da8-8971-d7e486613705;
					}
					- m_pParent = GUID 30b86204-7654-490a-aee3-e3c056b75669;
					- m_name = { CGIText 
						- m_str = "System::fsl_port_hal";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.102205 0 0 0.056263 715.7 413.239 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_bFramesetModified = 1;
					- m_polygon = 4 2 329  2 1451  1061 1451  1061 329  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=53%,47%>
<frame name=AttributeListCompartment>
<frame name=PrimitiveOperationListCompartment>";
					- Attrs = { IRPYRawContainer 
						- size = 0;
					}
					- Operations = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIClass 
					- _id = GUID c6fed933-846f-4b1e-bcee-5db64c97cf9f;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Class";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "Font.Size";
												- _Value = "8";
												- _Type = Int;
											}
										}
									}
								}
							}
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 87;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "System.sbs";
						- _subsystem = "System";
						- _class = "";
						- _name = "fsl_pwm_driver";
						- _id = GUID 7b65058d-9a67-44af-8030-5a1b3b5ef414;
					}
					- m_pParent = GUID 30b86204-7654-490a-aee3-e3c056b75669;
					- m_name = { CGIText 
						- m_str = "System::fsl_pwm_driver";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.113096 0 0 0.056263 1471.99 497.926 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 2 329  2 1451  1061 1451  1061 329  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=50%,50%>
<frame name=AttributeListCompartment>
<frame name=PrimitiveOperationListCompartment>";
					- Attrs = { IRPYRawContainer 
						- size = 0;
					}
					- Operations = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIClass 
					- _id = GUID 6515ce26-c133-4379-90a0-dd8d77d706f8;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Class";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "Font.Size";
												- _Value = "8";
												- _Type = Int;
											}
										}
									}
								}
							}
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 87;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "System.sbs";
						- _subsystem = "System";
						- _class = "";
						- _name = "fsl_smc_hal";
						- _id = GUID f3824b3c-1e2e-46a5-a755-f035a2bf2d78;
					}
					- m_pParent = GUID 30b86204-7654-490a-aee3-e3c056b75669;
					- m_name = { CGIText 
						- m_str = "System::fsl_smc_hal";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.102205 0 0 0.056263 835.95 413.613 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 2 329  2 1451  1061 1451  1061 329  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=50%,50%>
<frame name=AttributeListCompartment>
<frame name=PrimitiveOperationListCompartment>";
					- Attrs = { IRPYRawContainer 
						- size = 0;
					}
					- Operations = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIClass 
					- _id = GUID cd5f344e-b37b-4bb6-8075-1749de645be2;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Class";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "Font.Size";
												- _Value = "8";
												- _Type = Int;
											}
										}
									}
								}
							}
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 87;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "System.sbs";
						- _subsystem = "System";
						- _class = "";
						- _name = "fsl_tpm_driver";
						- _id = GUID bc7725aa-2f14-4531-be47-acc69d2f5971;
					}
					- m_pParent = GUID 30b86204-7654-490a-aee3-e3c056b75669;
					- m_name = { CGIText 
						- m_str = "System::fsl_tpm_driver";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.113561 0 0 0.056263 1399.52 353.301 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 2 329  2 1451  1061 1451  1061 329  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=50%,50%>
<frame name=AttributeListCompartment>
<frame name=PrimitiveOperationListCompartment>";
					- Attrs = { IRPYRawContainer 
						- size = 0;
					}
					- Operations = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIClass 
					- _id = GUID 83d40b69-423c-40e1-aa17-211583afebfb;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Class";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "Font.Size";
												- _Value = "8";
												- _Type = Int;
											}
										}
									}
								}
							}
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 87;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "System.sbs";
						- _subsystem = "System";
						- _class = "";
						- _name = "fsl_tpm_hal";
						- _id = GUID 9d1f00c7-f44e-4c29-a28f-249bba32e5e7;
					}
					- m_pParent = GUID 30b86204-7654-490a-aee3-e3c056b75669;
					- m_name = { CGIText 
						- m_str = "System::fsl_tpm_hal";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.101276 0 0 0.056263 1436.03 425.988 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 2 329  2 1451  1061 1451  1061 329  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=50%,50%>
<frame name=AttributeListCompartment>
<frame name=PrimitiveOperationListCompartment>";
					- Attrs = { IRPYRawContainer 
						- size = 0;
					}
					- Operations = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIClass 
					- _id = GUID a0236fbe-b1d3-4b1f-9a96-3f7987100c8d;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Class";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "Font.Size";
												- _Value = "8";
												- _Type = Int;
											}
										}
									}
								}
							}
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 87;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "System.sbs";
						- _subsystem = "System";
						- _class = "";
						- _name = "MKL25Z4";
						- _id = GUID ec95fed1-0393-4a7a-a9e1-26636f4463c2;
					}
					- m_pParent = GUID 30b86204-7654-490a-aee3-e3c056b75669;
					- m_name = { CGIText 
						- m_str = "System::MKL25Z4";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.0912708 0 0 0.056263 1951.56 413.675 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 2 329  2 1451  1061 1451  1061 329  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=50%,50%>
<frame name=AttributeListCompartment>
<frame name=PrimitiveOperationListCompartment>";
					- Attrs = { IRPYRawContainer 
						- size = 0;
					}
					- Operations = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIClass 
					- _id = GUID 1f185bb4-dde0-4611-9968-3b7ef2143784;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Class";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "Font.Size";
												- _Value = "8";
												- _Type = Int;
											}
										}
									}
								}
							}
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 87;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "System.sbs";
						- _subsystem = "System";
						- _class = "";
						- _name = "stdlib";
						- _id = GUID a5d29dcf-74ce-4b4b-bcba-940ae187d551;
					}
					- m_pParent = GUID 30b86204-7654-490a-aee3-e3c056b75669;
					- m_name = { CGIText 
						- m_str = "System::stdlib";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.0903932 0 0 0.056263 1604.09 413.362 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 2 329  2 1451  1061 1451  1061 329  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=50%,50%>
<frame name=AttributeListCompartment>
<frame name=PrimitiveOperationListCompartment>";
					- Attrs = { IRPYRawContainer 
						- size = 0;
					}
					- Operations = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIClass 
					- _id = GUID b5f6a8dc-1dcf-476a-9445-9ca434ee7a7f;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Class";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "Font.Size";
												- _Value = "10";
												- _Type = Int;
											}
										}
									}
								}
							}
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 87;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "main.sbs";
						- _subsystem = "Sources::main";
						- _class = "";
						- _name = "ES770";
						- _id = GUID afe21977-27c6-4112-82f8-abf04fcae452;
					}
					- m_pParent = GUID 30b86204-7654-490a-aee3-e3c056b75669;
					- m_name = { CGIText 
						- m_str = "main::ES770";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2152;
					- m_transform = 0.260469 0 0 0.0962564 235.479 508.331 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_bFramesetModified = 1;
					- m_polygon = 4 2 329  2 1451  1061 1451  1061 329  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=0%,100%>
<frame name=AttributeListCompartment>
<frame name=PrimitiveOperationListCompartment>";
					- Attrs = { IRPYRawContainer 
						- size = 0;
					}
					- Operations = { IRPYRawContainer 
						- size = 3;
						- value = 
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "main.sbs";
							- _subsystem = "Sources::main";
							- _class = "ES770";
							- _name = "main()";
							- _id = GUID 87115d89-1243-4fec-89d5-d9f736063178;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "main.sbs";
							- _subsystem = "Sources::main";
							- _class = "ES770";
							- _name = "initBoard()";
							- _id = GUID b6ed57e9-423f-43da-8eff-f580cc11c62c;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "main.sbs";
							- _subsystem = "Sources::main";
							- _class = "ES770";
							- _name = "initPeripherals()";
							- _id = GUID adbce8d6-94c7-4fcd-84fa-4e19d16a2454;
						}
					}
				}
				{ CGIClass 
					- _id = GUID 8809397d-2024-4fcf-bf49-a9c2cd53a733;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Class";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "Font.Size";
												- _Value = "10";
												- _Type = Int;
											}
										}
									}
								}
							}
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 87;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "controller.sbs";
						- _subsystem = "Sources::hal::controller";
						- _class = "";
						- _name = "controller";
						- _id = GUID 7aba1f16-a032-4bfe-ba75-f25185866ece;
					}
					- m_pParent = GUID 30b86204-7654-490a-aee3-e3c056b75669;
					- m_name = { CGIText 
						- m_str = "hal::controller::controller";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2152;
					- m_transform = 0.65069 0 0 0.160427 238.567 1487.22 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_bFramesetModified = 1;
					- m_polygon = 4 2 329  2 1451  1061 1451  1061 329  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=9%,91%>
<frame name=AttributeListCompartment>
<frame name=PrimitiveOperationListCompartment>";
					- Attrs = { IRPYRawContainer 
						- size = 0;
					}
					- Operations = { IRPYRawContainer 
						- size = 6;
						- value = 
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "controller.sbs";
							- _subsystem = "Sources::hal::controller";
							- _class = "controller";
							- _name = "initPID(contoller_instance_t)";
							- _id = GUID b06aae3e-d241-438c-8f04-01714432d456;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "controller.sbs";
							- _subsystem = "Sources::hal::controller";
							- _class = "controller";
							- _name = "setMaxSumError(contoller_instance_t,double)";
							- _id = GUID c5d01870-778d-46d8-a158-8c3623fb7f39;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "controller.sbs";
							- _subsystem = "Sources::hal::controller";
							- _class = "controller";
							- _name = "setKp(contoller_instance_t,double)";
							- _id = GUID 874db528-c62d-4aeb-9446-b27e18187a0d;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "controller.sbs";
							- _subsystem = "Sources::hal::controller";
							- _class = "controller";
							- _name = "setKd(contoller_instance_t,double)";
							- _id = GUID 1f1724f5-3975-48c7-962b-2d11f48d083d;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "controller.sbs";
							- _subsystem = "Sources::hal::controller";
							- _class = "controller";
							- _name = "setKi(contoller_instance_t,double)";
							- _id = GUID c731650a-ddca-4974-a5d2-e95dc0a6cd3d;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "controller.sbs";
							- _subsystem = "Sources::hal::controller";
							- _class = "controller";
							- _name = "PIDupdate(contoller_instance_t,double,double)";
							- _id = GUID 2ce5c826-097b-4550-8a2c-198c83fdbd65;
						}
					}
				}
				{ CGIClass 
					- _id = GUID 0634619c-fa98-4356-b802-05bb417607b5;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Class";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "Font.Size";
												- _Value = "10";
												- _Type = Int;
											}
										}
									}
								}
							}
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 87;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "driver.sbs";
						- _subsystem = "Sources::hal::driver";
						- _class = "";
						- _name = "driver";
						- _id = GUID a1a6b9cd-8122-46e8-acff-e1b619884d5b;
					}
					- m_pParent = GUID 30b86204-7654-490a-aee3-e3c056b75669;
					- m_name = { CGIText 
						- m_str = "hal::driver::driver";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2152;
					- m_transform = 0.602098 0 0 0.205883 238.837 1200.27 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_bFramesetModified = 1;
					- m_polygon = 4 2 329  2 1451  1061 1451  1061 329  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=11%,89%>
<frame name=AttributeListCompartment>
<frame name=PrimitiveOperationListCompartment>";
					- Attrs = { IRPYRawContainer 
						- size = 0;
					}
					- Operations = { IRPYRawContainer 
						- size = 9;
						- value = 
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "driver.sbs";
							- _subsystem = "Sources::hal::driver";
							- _class = "driver";
							- _name = "initDriver(driver_instance_t)";
							- _id = GUID 90882407-f609-406e-a9da-e0bb19a6a4a2;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "driver.sbs";
							- _subsystem = "Sources::hal::driver";
							- _class = "driver";
							- _name = "disableDriver(driver_instance_t)";
							- _id = GUID 874b84c1-d27d-4def-9ff6-4e02c1395fe6;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "driver.sbs";
							- _subsystem = "Sources::hal::driver";
							- _class = "driver";
							- _name = "enable_driver(driver_instance_t)";
							- _id = GUID ad5c544b-29fa-46e2-be4a-74bdc64e1ff6;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "driver.sbs";
							- _subsystem = "Sources::hal::driver";
							- _class = "driver";
							- _name = "setHBridgeDutyCycle(driver_instance_t,unsigned int)";
							- _id = GUID 751c6651-fe54-4165-be3d-a8f4c9e7de2d;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "driver.sbs";
							- _subsystem = "Sources::hal::driver";
							- _class = "driver";
							- _name = "setDriver(driver_instance_t,int)";
							- _id = GUID ebc8bb19-731f-4427-893f-a94fcdedd64a;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "driver.sbs";
							- _subsystem = "Sources::hal::driver";
							- _class = "driver";
							- _name = "appendDriver(driver_instance_t)";
							- _id = GUID 8aae3ace-bec9-4c02-885e-d78b6593a907;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "driver.sbs";
							- _subsystem = "Sources::hal::driver";
							- _class = "driver";
							- _name = "setChannelADutyCycle(driver_instance_t,int)";
							- _id = GUID 34b7a0b9-1cf8-4618-a443-f4f5f020eecc;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "driver.sbs";
							- _subsystem = "Sources::hal::driver";
							- _class = "driver";
							- _name = "Operation_46()";
							- _id = GUID fad5db8d-d42e-4dce-91b7-9138ef665360;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "driver.sbs";
							- _subsystem = "Sources::hal::driver";
							- _class = "driver";
							- _name = "setChannelBDutyCycle(driver_instance_t,int)";
							- _id = GUID 1bbdafcd-f720-4745-a8e4-e6072b4f4352;
						}
					}
				}
				{ CGIClass 
					- _id = GUID 14cc5e3d-9af8-4d47-94a5-581348d066e0;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Class";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "Font.Size";
												- _Value = "10";
												- _Type = Int;
											}
										}
									}
								}
							}
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 87;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "encoder.sbs";
						- _subsystem = "Sources::hal::encoder";
						- _class = "";
						- _name = "encoder";
						- _id = GUID a4d29078-1f9a-4eab-b77d-531261e23fc1;
					}
					- m_pParent = GUID 30b86204-7654-490a-aee3-e3c056b75669;
					- m_name = { CGIText 
						- m_str = "hal::encoder::encoder";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2152;
					- m_transform = 0.547362 0 0 0.227272 242.927 905.228 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_bFramesetModified = 1;
					- m_polygon = 4 2 329  2 1451  1061 1451  1061 329  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=8%,92%>
<frame name=AttributeListCompartment>
<frame name=PrimitiveOperationListCompartment>";
					- Attrs = { IRPYRawContainer 
						- size = 0;
					}
					- Operations = { IRPYRawContainer 
						- size = 10;
						- value = 
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "encoder.sbs";
							- _subsystem = "Sources::hal::encoder";
							- _class = "encoder";
							- _name = "initEncoder(encoder_instance_t)";
							- _id = GUID bbcd7720-dad3-475c-8728-545dc18fdb12;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "encoder.sbs";
							- _subsystem = "Sources::hal::encoder";
							- _class = "encoder";
							- _name = "enableCounter(encoder_instance_t)";
							- _id = GUID c90f0de0-4578-4485-bb08-f1f3fb03fb29;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "encoder.sbs";
							- _subsystem = "Sources::hal::encoder";
							- _class = "encoder";
							- _name = "disableCounter(encoder_instance_t)";
							- _id = GUID 4d5c8a03-e21a-4de8-bdb5-8205c47dabe8;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "encoder.sbs";
							- _subsystem = "Sources::hal::encoder";
							- _class = "encoder";
							- _name = "resetCounter(encoder_instance_t)";
							- _id = GUID 5933c073-bf37-4e38-86c8-9683f0e85eef;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "encoder.sbs";
							- _subsystem = "Sources::hal::encoder";
							- _class = "encoder";
							- _name = "getAngularVelocityRPM(encoder_instance_t)";
							- _id = GUID 917afde4-520b-45e0-87c8-9053718f25c0;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "encoder.sbs";
							- _subsystem = "Sources::hal::encoder";
							- _class = "encoder";
							- _name = "getAngularVelocityRad(encoder_instance_t)";
							- _id = GUID 51cfdee8-c26a-4c06-8090-f780117c71ed;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "encoder.sbs";
							- _subsystem = "Sources::hal::encoder";
							- _class = "encoder";
							- _name = "getDirection(encoder_instance_t)";
							- _id = GUID c36292ca-3efd-48b7-b340-a9e6d83a2f30;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "encoder.sbs";
							- _subsystem = "Sources::hal::encoder";
							- _class = "encoder";
							- _name = "takeMeasurement(encoder_instance_t)";
							- _id = GUID aa36e3a6-5ef6-4a63-9dc7-a24c29faad11;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "encoder.sbs";
							- _subsystem = "Sources::hal::encoder";
							- _class = "encoder";
							- _name = "getAngularVelocity(encoder_instance_t)";
							- _id = GUID b5b59a5f-3157-4b57-bd8c-7d04e9f70a53;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "encoder.sbs";
							- _subsystem = "Sources::hal::encoder";
							- _class = "encoder";
							- _name = "enableChOInterrupt(encoder_instance_t)";
							- _id = GUID 05e0aa51-e41c-4fc6-b2f5-b6ec41515029;
						}
					}
				}
				{ CGIClass 
					- _id = GUID 3f1f93f1-6e49-46b1-9c09-b94e874b0752;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Class";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "Font.Size";
												- _Value = "10";
												- _Type = Int;
											}
										}
									}
								}
							}
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 87;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "mcg.sbs";
						- _subsystem = "Sources::hal::mcg";
						- _class = "";
						- _name = "mcg";
						- _id = GUID a73cfdca-b18e-4872-9e19-c1e04af65df1;
					}
					- m_pParent = GUID 30b86204-7654-490a-aee3-e3c056b75669;
					- m_name = { CGIText 
						- m_str = "hal::mcg::mcg";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2088;
					- m_transform = 0.261122 0 0 0.106952 235.144 360.813 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_bFramesetModified = 1;
					- m_polygon = 4 2 329  2 1451  1061 1451  1061 329  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=56%,44%>
<frame name=AttributeListCompartment>
<frame name=PrimitiveOperationListCompartment>";
					- Attrs = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "mcg.sbs";
							- _subsystem = "Sources::hal::mcg";
							- _class = "mcg";
							- _name = "OSC0_XTAL_FREQ";
							- _id = GUID 3059acc4-6234-49e8-a2db-392813fde4d6;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "mcg.sbs";
							- _subsystem = "Sources::hal::mcg";
							- _class = "mcg";
							- _name = "RTC_XTAL_FREQ";
							- _id = GUID 1f03d55d-3e68-4148-af0e-51c9fb7b2027;
						}
					}
					- Operations = { IRPYRawContainer 
						- size = 1;
						- value = 
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "mcg.sbs";
							- _subsystem = "Sources::hal::mcg";
							- _class = "mcg";
							- _name = "mcg_clockInit()";
							- _id = GUID b98f5f33-7af5-4eec-8e18-b6d50e70e48e;
						}
					}
				}
				{ CGIClass 
					- _id = GUID ae6090bb-89f7-4802-8fbf-d9d3793b27f1;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Class";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "Font.Size";
												- _Value = "10";
												- _Type = Int;
											}
										}
									}
								}
							}
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 87;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "util.sbs";
						- _subsystem = "Sources::hal::util";
						- _class = "";
						- _name = "tc_hal";
						- _id = GUID 57a158ce-caa1-4896-8f55-0c6ddcaca961;
					}
					- m_pParent = GUID 30b86204-7654-490a-aee3-e3c056b75669;
					- m_name = { CGIText 
						- m_str = "hal::util::tc_hal";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2152;
					- m_transform = 0.496401 0 0 0.0695187 559.319 325.128 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_bFramesetModified = 1;
					- m_polygon = 4 2 329  2 1451  1061 1451  1061 329  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=23%,77%>
<frame name=AttributeListCompartment>
<frame name=PrimitiveOperationListCompartment>";
					- Attrs = { IRPYRawContainer 
						- size = 0;
					}
					- Operations = { IRPYRawContainer 
						- size = 1;
						- value = 
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "util.sbs";
							- _subsystem = "Sources::hal::util";
							- _class = "tc_hal";
							- _name = "installLptmr0(unsigned int,lptmr_callback_t)";
							- _id = GUID 6a338f0a-9b33-424b-a491-dba6759bccec;
						}
					}
				}
				{ CGIClass 
					- _id = GUID da185fd8-2eb7-44de-ab23-fc7519e2e0bb;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 87;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "target_definitions.sbs";
						- _subsystem = "Sources::hal::target_definitions";
						- _class = "";
						- _name = "target_pins";
						- _id = GUID d27ea60b-073d-49d5-9595-2e38935d2c0a;
					}
					- m_pParent = GUID 30b86204-7654-490a-aee3-e3c056b75669;
					- m_name = { CGIText 
						- m_str = "hal::target_definitions::target_pins";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2152;
					- m_transform = 0.497639 0 0 1.34759 1907 460.642 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_bFramesetModified = 1;
					- m_polygon = 4 2 329  2 1451  1061 1451  1061 329  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=99%,1%>
<frame name=AttributeListCompartment>
<frame name=PrimitiveOperationListCompartment>";
					- Attrs = { IRPYRawContainer 
						- size = 84;
						- value = 
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "target_definitions.sbs";
							- _subsystem = "Sources::hal::target_definitions";
							- _class = "target_pins";
							- _name = "DRIVER_LW_CHA_INSTANCE";
							- _id = GUID f3310c0e-3894-4cc8-8b3f-6255dfe8bc61;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "target_definitions.sbs";
							- _subsystem = "Sources::hal::target_definitions";
							- _class = "target_pins";
							- _name = "DRIVER_LW_CHA_PIN_NUMBER";
							- _id = GUID 090c6d63-524e-442c-aabd-598924b4470c;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "target_definitions.sbs";
							- _subsystem = "Sources::hal::target_definitions";
							- _class = "target_pins";
							- _name = "DRIVER_LW_CHA_PORT_ALT";
							- _id = GUID cb71fa5e-d6e1-40f8-8d9c-3f60e8c7e3ce;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "target_definitions.sbs";
							- _subsystem = "Sources::hal::target_definitions";
							- _class = "target_pins";
							- _name = "DRIVER_LW_CHA_PORT_INSTANCE";
							- _id = GUID e884fc12-604b-493d-84c0-18eec37d7a56;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "target_definitions.sbs";
							- _subsystem = "Sources::hal::target_definitions";
							- _class = "target_pins";
							- _name = "DRIVER_RW_CHA_INSTANCE";
							- _id = GUID fd694909-e7ac-487c-b930-c1ba8ccc2c8b;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "target_definitions.sbs";
							- _subsystem = "Sources::hal::target_definitions";
							- _class = "target_pins";
							- _name = "DRIVER_RW_CHA_PIN_NUMBER";
							- _id = GUID d9779c1b-4ace-431c-86f1-b3cf2b750428;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "target_definitions.sbs";
							- _subsystem = "Sources::hal::target_definitions";
							- _class = "target_pins";
							- _name = "DRIVER_RW_CHA_PORT_ALT";
							- _id = GUID 01635efa-ab0b-4dca-b387-6404843ad193;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "target_definitions.sbs";
							- _subsystem = "Sources::hal::target_definitions";
							- _class = "target_pins";
							- _name = "DRIVER_RW_CHA_PORT_INSTANCE";
							- _id = GUID 2d75b586-7361-4b9c-890b-a10ad9a94b89;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "target_definitions.sbs";
							- _subsystem = "Sources::hal::target_definitions";
							- _class = "target_pins";
							- _name = "DRIVER_RW_EN_PIN_NUMBER";
							- _id = GUID fb69a7fa-af2a-4804-acdd-5867f9cac24e;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "target_definitions.sbs";
							- _subsystem = "Sources::hal::target_definitions";
							- _class = "target_pins";
							- _name = "DRIVER_RW_EN_PORT_ALT";
							- _id = GUID 2c8473f9-2275-4739-a95d-e62f9a90424c;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "target_definitions.sbs";
							- _subsystem = "Sources::hal::target_definitions";
							- _class = "target_pins";
							- _name = "DRIVER_RW_EN_PORT_GPIO_INSTANCE";
							- _id = GUID 79a80c54-ac19-44d6-a678-5659a608384e;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "target_definitions.sbs";
							- _subsystem = "Sources::hal::target_definitions";
							- _class = "target_pins";
							- _name = "ENCODER_RW_PIN_NUMBER";
							- _id = GUID 5952e305-b00a-44c4-a783-c60c80a41232;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "target_definitions.sbs";
							- _subsystem = "Sources::hal::target_definitions";
							- _class = "target_pins";
							- _name = "ENCODER_RW_PORT_ALT";
							- _id = GUID 43fdbdd1-bf28-42d6-92c9-96a62b828465;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "target_definitions.sbs";
							- _subsystem = "Sources::hal::target_definitions";
							- _class = "target_pins";
							- _name = "ENCODER_RW_PORT_INSTANCE";
							- _id = GUID 2d4d8197-6ff0-4c65-8412-83fbab3e29dd;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "target_definitions.sbs";
							- _subsystem = "Sources::hal::target_definitions";
							- _class = "target_pins";
							- _name = "ENCODER_RW_TPM_INSTANCE";
							- _id = GUID f7b18fc2-8885-4378-9ee3-fa40f8e8b78c;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "target_definitions.sbs";
							- _subsystem = "Sources::hal::target_definitions";
							- _class = "target_pins";
							- _name = "ENCODER_LW_PIN_NUMBER";
							- _id = GUID 1870e462-3c3b-4511-87fd-66ba247fec47;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "target_definitions.sbs";
							- _subsystem = "Sources::hal::target_definitions";
							- _class = "target_pins";
							- _name = "ENCODER_LW_PORT_ALT";
							- _id = GUID c38793d4-5a3e-4c38-934d-e9188b1b5b4c;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "target_definitions.sbs";
							- _subsystem = "Sources::hal::target_definitions";
							- _class = "target_pins";
							- _name = "ENCODER_LW_PORT_INSTANCE";
							- _id = GUID 993a7d4f-b350-4bb2-bef8-1f9cb1134a8c;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "target_definitions.sbs";
							- _subsystem = "Sources::hal::target_definitions";
							- _class = "target_pins";
							- _name = "ENCODER_LW_TPM_INSTANCE";
							- _id = GUID 25306d9b-130e-44a0-b5cf-fbbb48621062;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "target_definitions.sbs";
							- _subsystem = "Sources::hal::target_definitions";
							- _class = "target_pins";
							- _name = "ENCODER_RW_FTM_CLKIN_SRC";
							- _id = GUID 9f50e991-882b-44a9-a323-5b44ad18678a;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "target_definitions.sbs";
							- _subsystem = "Sources::hal::target_definitions";
							- _class = "target_pins";
							- _name = "ENCODER_LW_FTM_CLKIN_SRC";
							- _id = GUID 4ed8b16d-0e41-49e3-9e1e-b07babbc443d;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "target_definitions.sbs";
							- _subsystem = "Sources::hal::target_definitions";
							- _class = "target_pins";
							- _name = "GPIO_OUTPUT";
							- _id = GUID 4f36b0e7-7907-43f8-af09-53126e91a940;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "target_definitions.sbs";
							- _subsystem = "Sources::hal::target_definitions";
							- _class = "target_pins";
							- _name = "GPIO_INPUT";
							- _id = GUID 09f73c2e-26f5-42f8-a88d-7d6d04f8548d;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "target_definitions.sbs";
							- _subsystem = "Sources::hal::target_definitions";
							- _class = "target_pins";
							- _name = "CONST_2PI";
							- _id = GUID 1afdc0ac-39b3-4a55-8065-8130bf30a243;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "target_definitions.sbs";
							- _subsystem = "Sources::hal::target_definitions";
							- _class = "target_pins";
							- _name = "CYCLIC_EXECUTIVE_PERIOD";
							- _id = GUID a058288d-31aa-4a8d-a4e6-878c7e198991;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "target_definitions.sbs";
							- _subsystem = "Sources::hal::target_definitions";
							- _class = "target_pins";
							- _name = "DRIVER_EN_PIN_DIR";
							- _id = GUID 25aa36e0-d243-4ab2-b469-b4da2d79de0e;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "target_definitions.sbs";
							- _subsystem = "Sources::hal::target_definitions";
							- _class = "target_pins";
							- _name = "HMI_UART_PORT_INSTANCE";
							- _id = GUID 3958e7cf-a0aa-4223-b8f8-39a5d4148a83;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "target_definitions.sbs";
							- _subsystem = "Sources::hal::target_definitions";
							- _class = "target_pins";
							- _name = "HMI_UART_PIN_RX";
							- _id = GUID 34514e71-e8cd-4bc3-984a-9f9eec27b5eb;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "target_definitions.sbs";
							- _subsystem = "Sources::hal::target_definitions";
							- _class = "target_pins";
							- _name = "HMI_UART_PIN_TX";
							- _id = GUID 75306260-445c-44b1-84a1-5c9b6f1fb294;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "target_definitions.sbs";
							- _subsystem = "Sources::hal::target_definitions";
							- _class = "target_pins";
							- _name = "HMI_UART_INSTANCE";
							- _id = GUID 3b39979c-38ff-4d9f-abf6-5b737d4d1a5b;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "target_definitions.sbs";
							- _subsystem = "Sources::hal::target_definitions";
							- _class = "target_pins";
							- _name = "HMI_UART_BASE";
							- _id = GUID 8f27f6ef-f6e4-43ad-ac66-bfa732067e2f;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "target_definitions.sbs";
							- _subsystem = "Sources::hal::target_definitions";
							- _class = "target_pins";
							- _name = "HMI_UART_BAUD";
							- _id = GUID fb565bcb-bfa7-45e0-865c-f7ef556a7fce;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "target_definitions.sbs";
							- _subsystem = "Sources::hal::target_definitions";
							- _class = "target_pins";
							- _name = "HMI_UART_PIN_ALT";
							- _id = GUID 748034e9-da5f-4c79-a53b-68856920b476;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "target_definitions.sbs";
							- _subsystem = "Sources::hal::target_definitions";
							- _class = "target_pins";
							- _name = "DRIVER_LW_CHB_INSTANCE";
							- _id = GUID 6a3b973d-baa3-4109-83c5-914383a33f26;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "target_definitions.sbs";
							- _subsystem = "Sources::hal::target_definitions";
							- _class = "target_pins";
							- _name = "DRIVER_LW_CHB_PIN_NUMBER";
							- _id = GUID 2fb7a8dc-8a8c-48d3-b602-7c4be7edd3ea;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "target_definitions.sbs";
							- _subsystem = "Sources::hal::target_definitions";
							- _class = "target_pins";
							- _name = "DRIVER_LW_CHB_PORT_ALT";
							- _id = GUID 9f16b761-390c-4845-b63c-7956407df8ef;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "target_definitions.sbs";
							- _subsystem = "Sources::hal::target_definitions";
							- _class = "target_pins";
							- _name = "DRIVER_LW_CHB_PORT_INSTANCE";
							- _id = GUID de7eb526-1672-43db-9fbb-14f51d8702a8;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "target_definitions.sbs";
							- _subsystem = "Sources::hal::target_definitions";
							- _class = "target_pins";
							- _name = "DRIVER_RW_CHB_INSTANCE";
							- _id = GUID 9c78c42d-1e99-47bd-9c35-f3ccab298eab;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "target_definitions.sbs";
							- _subsystem = "Sources::hal::target_definitions";
							- _class = "target_pins";
							- _name = "DRIVER_RW_CHB_PIN_NUMBER";
							- _id = GUID f5fc36f1-cbbd-450d-80fc-e0dd2f919af2;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "target_definitions.sbs";
							- _subsystem = "Sources::hal::target_definitions";
							- _class = "target_pins";
							- _name = "DRIVER_RW_CHB_PORT_ALT";
							- _id = GUID c9da1155-9a88-43ec-82a0-b9fdf3e0808a;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "target_definitions.sbs";
							- _subsystem = "Sources::hal::target_definitions";
							- _class = "target_pins";
							- _name = "DRIVER_RW_CHB_PORT_INSTANCE";
							- _id = GUID 3294f667-bfb9-42b3-aabf-42170682f143;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "target_definitions.sbs";
							- _subsystem = "Sources::hal::target_definitions";
							- _class = "target_pins";
							- _name = "DRIVER_LW_EN_PIN_NUMBER";
							- _id = GUID b1b0d014-a458-413e-9cfe-7de813d1c8cb;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "target_definitions.sbs";
							- _subsystem = "Sources::hal::target_definitions";
							- _class = "target_pins";
							- _name = "DRIVER_LW_EN_PORT_ALT";
							- _id = GUID 2d2d8b8c-0d48-4fe2-831b-223771eb1e6b;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "target_definitions.sbs";
							- _subsystem = "Sources::hal::target_definitions";
							- _class = "target_pins";
							- _name = "DRIVER_LW_EN_PORT_INSTANCE";
							- _id = GUID 703682c2-0923-405f-b6cc-b7edf801f079;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "target_definitions.sbs";
							- _subsystem = "Sources::hal::target_definitions";
							- _class = "target_pins";
							- _name = "DRIVER_RW_TPM_CLKIN_INSTANCE";
							- _id = GUID 27503a74-3ef8-4dcb-a31f-ac803031ba88;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "target_definitions.sbs";
							- _subsystem = "Sources::hal::target_definitions";
							- _class = "target_pins";
							- _name = "DRIVER_RW_TPM_INSTANCE";
							- _id = GUID 3c4950bd-455a-4e15-bf83-73bb8d8f1f39;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "target_definitions.sbs";
							- _subsystem = "Sources::hal::target_definitions";
							- _class = "target_pins";
							- _name = "DRIVER_LW_TPM_CLKIN_INSTANCE";
							- _id = GUID 5b6d7e1f-eb3c-4ddd-881c-88799055b0b2;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "target_definitions.sbs";
							- _subsystem = "Sources::hal::target_definitions";
							- _class = "target_pins";
							- _name = "DRIVER_LW_TPM_INSTANCE";
							- _id = GUID 4297dc6f-8634-4778-ac53-aa5ee1279880;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "target_definitions.sbs";
							- _subsystem = "Sources::hal::target_definitions";
							- _class = "target_pins";
							- _name = "DRIVER_RW_TPM_CLK_SRC";
							- _id = GUID 824727d5-869f-41d0-b415-7638cf33055d;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "target_definitions.sbs";
							- _subsystem = "Sources::hal::target_definitions";
							- _class = "target_pins";
							- _name = "DRIVER_LW_TPM_CLK_SRC";
							- _id = GUID 7b4f0a8b-ea2e-4de3-b9b9-fe8c847bc5f0;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "target_definitions.sbs";
							- _subsystem = "Sources::hal::target_definitions";
							- _class = "target_pins";
							- _name = "DRIVER_RW_TPM_CLK_PS";
							- _id = GUID 59bf54f9-3081-499c-84c8-289eb560b88e;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "target_definitions.sbs";
							- _subsystem = "Sources::hal::target_definitions";
							- _class = "target_pins";
							- _name = "DRIVER_LW_TPM_CLK_PS";
							- _id = GUID 12c09f8d-5631-48f0-a1b3-6232d00ff213;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "target_definitions.sbs";
							- _subsystem = "Sources::hal::target_definitions";
							- _class = "target_pins";
							- _name = "DRIVER_LW_EN_GPIO_INSTANCE";
							- _id = GUID c82557fe-6426-48cb-996b-fd7b583b2a93;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "target_definitions.sbs";
							- _subsystem = "Sources::hal::target_definitions";
							- _class = "target_pins";
							- _name = "DRIVER_RW_EN_GPIO_INSTANCE";
							- _id = GUID 4f4e63f8-1280-4f63-948b-bb59745301cc;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "target_definitions.sbs";
							- _subsystem = "Sources::hal::target_definitions";
							- _class = "target_pins";
							- _name = "DEBUG_MODE_ENABLE";
							- _id = GUID be5fc4d0-e7ff-4f76-ad05-13ae969e913a;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "target_definitions.sbs";
							- _subsystem = "Sources::hal::target_definitions";
							- _class = "target_pins";
							- _name = "MAX_RW_MOTOR_VELOCITY_RAD";
							- _id = GUID 8dd39182-a32c-4d43-9fe1-b1582facc642;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "target_definitions.sbs";
							- _subsystem = "Sources::hal::target_definitions";
							- _class = "target_pins";
							- _name = "MAX_LW_MOTOR_VELOCITY_RAD";
							- _id = GUID ebc30a95-b2b3-4add-a04f-2a321b54e8d9;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "target_definitions.sbs";
							- _subsystem = "Sources::hal::target_definitions";
							- _class = "target_pins";
							- _name = "ENCODER_RW_MAX_PULSE_COUNT";
							- _id = GUID dc8d7844-891a-4344-9cc3-03cae96cf7f3;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "target_definitions.sbs";
							- _subsystem = "Sources::hal::target_definitions";
							- _class = "target_pins";
							- _name = "ENCODER_RW_PULSE_COUNT";
							- _id = GUID 5f35e49d-bcf9-4bd9-9aeb-a1fe8ace15e0;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "target_definitions.sbs";
							- _subsystem = "Sources::hal::target_definitions";
							- _class = "target_pins";
							- _name = "ENCODER_RW_ACQ_PERIOD_US";
							- _id = GUID c55d631c-3046-401c-8135-4861d1d09919;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "target_definitions.sbs";
							- _subsystem = "Sources::hal::target_definitions";
							- _class = "target_pins";
							- _name = "ENCODER_LW_MAX_PULSE_COUNT";
							- _id = GUID 7500740c-75bc-401f-9716-ebe24b361f25;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "target_definitions.sbs";
							- _subsystem = "Sources::hal::target_definitions";
							- _class = "target_pins";
							- _name = "ENCODER_LW_PULSE_COUNT";
							- _id = GUID 7c8799f2-1dc9-4b70-be2a-b4c2848095d5;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "target_definitions.sbs";
							- _subsystem = "Sources::hal::target_definitions";
							- _class = "target_pins";
							- _name = "ENCODER_LW_ACQ_PERIOD_US";
							- _id = GUID 919ac9de-c591-442c-96e4-5c0cb35921dd;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "target_definitions.sbs";
							- _subsystem = "Sources::hal::target_definitions";
							- _class = "target_pins";
							- _name = "HMI_DIAG_BTN_PORT_INSTANCE";
							- _id = GUID fe6e0c33-efee-4954-ba09-53c28286854a;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "target_definitions.sbs";
							- _subsystem = "Sources::hal::target_definitions";
							- _class = "target_pins";
							- _name = "HMI_DIAG_BTN_PORT_ALT";
							- _id = GUID 7e6b2c0b-ff0c-4f23-bc3b-7bb2bbadf384;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "target_definitions.sbs";
							- _subsystem = "Sources::hal::target_definitions";
							- _class = "target_pins";
							- _name = "HMI_DIAG_BTN_IRQN";
							- _id = GUID e590e0dd-405f-4c66-8898-cf492d298280;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "target_definitions.sbs";
							- _subsystem = "Sources::hal::target_definitions";
							- _class = "target_pins";
							- _name = "HMI_DIAG_BTN_PIN_NUMBER";
							- _id = GUID e2fd3e0d-649e-4b8d-a244-668b8bbe094a;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "target_definitions.sbs";
							- _subsystem = "Sources::hal::target_definitions";
							- _class = "target_pins";
							- _name = "HMI_STOP_BTN_PORT_INSTANCE";
							- _id = GUID 35fd7709-5898-4698-9b08-e7dd8be9c2e0;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "target_definitions.sbs";
							- _subsystem = "Sources::hal::target_definitions";
							- _class = "target_pins";
							- _name = "HMI_STOP_BTN_IRQN";
							- _id = GUID 23ff92ea-d54a-4ffa-9569-281c2eaa236d;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "target_definitions.sbs";
							- _subsystem = "Sources::hal::target_definitions";
							- _class = "target_pins";
							- _name = "HMI_STOP_BTN_PORT_ALT";
							- _id = GUID 74bed94e-7cf5-4bc4-9700-c1b08497cb8d;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "target_definitions.sbs";
							- _subsystem = "Sources::hal::target_definitions";
							- _class = "target_pins";
							- _name = "HMI_STOP_BTN_PIN_NUMBER";
							- _id = GUID f5546888-2592-4565-b125-19969df79d9d;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "target_definitions.sbs";
							- _subsystem = "Sources::hal::target_definitions";
							- _class = "target_pins";
							- _name = "ADC_IR1_PORT_INSTANCE";
							- _id = GUID f0a36e2c-e4c5-41b2-b4a8-25b161cf2bfa;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "target_definitions.sbs";
							- _subsystem = "Sources::hal::target_definitions";
							- _class = "target_pins";
							- _name = "ADC_IR2_PORT_INSTANCE";
							- _id = GUID 775bb1d7-1924-48ed-b260-d671d34269dc;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "target_definitions.sbs";
							- _subsystem = "Sources::hal::target_definitions";
							- _class = "target_pins";
							- _name = "ADC_IR3_PORT_INSTANCE";
							- _id = GUID c958e373-5957-49bb-a09d-d405c8892622;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "target_definitions.sbs";
							- _subsystem = "Sources::hal::target_definitions";
							- _class = "target_pins";
							- _name = "ADC_IR4_PORT_INSTANCE";
							- _id = GUID fbac4b6a-f3b8-4f1b-b1c0-8a124a61b387;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "target_definitions.sbs";
							- _subsystem = "Sources::hal::target_definitions";
							- _class = "target_pins";
							- _name = "ADC_IR5_PORT_INSTANCE";
							- _id = GUID cf3dcaa9-4ac5-4c7e-979b-b3b74a1828e3;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "target_definitions.sbs";
							- _subsystem = "Sources::hal::target_definitions";
							- _class = "target_pins";
							- _name = "ADC_IR6_PORT_INSTANCE";
							- _id = GUID 47fe59ce-54a3-4cc8-a353-42f116009457;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "target_definitions.sbs";
							- _subsystem = "Sources::hal::target_definitions";
							- _class = "target_pins";
							- _name = "ADC_PORT_ALT";
							- _id = GUID 5e99045d-4daf-4526-b415-a904acfa8975;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "target_definitions.sbs";
							- _subsystem = "Sources::hal::target_definitions";
							- _class = "target_pins";
							- _name = "ADC_IR1_PIN_NUMBER";
							- _id = GUID e51efe3d-821d-428c-8722-e142ebf31102;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "target_definitions.sbs";
							- _subsystem = "Sources::hal::target_definitions";
							- _class = "target_pins";
							- _name = "ADC_IR2_PIN_NUMBER";
							- _id = GUID 7f249d5e-0da7-4606-be7c-ee13a24d4aba;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "target_definitions.sbs";
							- _subsystem = "Sources::hal::target_definitions";
							- _class = "target_pins";
							- _name = "ADC_IR3_PIN_NUMBER";
							- _id = GUID 1dad92bb-6203-4980-9022-2da65a3a31de;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "target_definitions.sbs";
							- _subsystem = "Sources::hal::target_definitions";
							- _class = "target_pins";
							- _name = "ADC_IR4_PIN_NUMBER";
							- _id = GUID 3b5165c7-20a0-4cc2-bbea-93c6fb1976b3;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "target_definitions.sbs";
							- _subsystem = "Sources::hal::target_definitions";
							- _class = "target_pins";
							- _name = "ADC_IR5_PIN_NUMBER";
							- _id = GUID 05afc046-1df1-48ca-8220-f0db7a82f0e3;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "target_definitions.sbs";
							- _subsystem = "Sources::hal::target_definitions";
							- _class = "target_pins";
							- _name = "ADC_IR6_PIN_NUMBER";
							- _id = GUID 6236759d-0c5d-4151-b504-bae562b0ae95;
						}
					}
					- Operations = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIClass 
					- _id = GUID 2b78bb12-b9a1-4b17-9fd2-0381d921e35a;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 87;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "hmi.sbs";
						- _subsystem = "Sources::hal::hmi";
						- _class = "";
						- _name = "hmi";
						- _id = GUID d2efe68a-9264-4677-ac93-14dc5079e94f;
					}
					- m_pParent = GUID 30b86204-7654-490a-aee3-e3c056b75669;
					- m_name = { CGIText 
						- m_str = "hal::hmi::hmi";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2088;
					- m_transform = 0.40321 0 0 0.202317 239.194 637.434 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_bFramesetModified = 1;
					- m_polygon = 4 2 329  2 1451  1061 1451  1061 329  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=11%,89%>
<frame name=AttributeListCompartment>
<frame name=PrimitiveOperationListCompartment>";
					- Attrs = { IRPYRawContainer 
						- size = 0;
					}
					- Operations = { IRPYRawContainer 
						- size = 8;
						- value = 
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "hmi.sbs";
							- _subsystem = "Sources::hal::hmi";
							- _class = "hmi";
							- _name = "transmitSISI(char*,int,char*,int)";
							- _id = GUID 1e1ba5ac-5c82-48a1-beec-fb5c6694aa38;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "hmi.sbs";
							- _subsystem = "Sources::hal::hmi";
							- _class = "hmi";
							- _name = "initHmi()";
							- _id = GUID 3441fdb3-e9dc-4c7f-b610-1180d7343ad8;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "hmi.sbs";
							- _subsystem = "Sources::hal::hmi";
							- _class = "hmi";
							- _name = "transmitNewLine()";
							- _id = GUID d478dd47-30b8-4301-8a70-f46bd017be3b;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "hmi.sbs";
							- _subsystem = "Sources::hal::hmi";
							- _class = "hmi";
							- _name = "transmitS(char*)";
							- _id = GUID a579df28-5369-4aa2-b1ce-0a0efc11a02a;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "hmi.sbs";
							- _subsystem = "Sources::hal::hmi";
							- _class = "hmi";
							- _name = "transmitSCS(char*,char,char*)";
							- _id = GUID 376a2bfb-32f2-472e-a728-6c7109c7514a;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "hmi.sbs";
							- _subsystem = "Sources::hal::hmi";
							- _class = "hmi";
							- _name = "transmitSCSF(char*,char,char*,float)";
							- _id = GUID 3efdbdbb-eb68-4efc-bd16-cc93e1530355;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "hmi.sbs";
							- _subsystem = "Sources::hal::hmi";
							- _class = "hmi";
							- _name = "receive()";
							- _id = GUID cc658a00-b6da-4b97-b39c-23edaaf5407b;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "hmi.sbs";
							- _subsystem = "Sources::hal::hmi";
							- _class = "hmi";
							- _name = "transmitIrArray(uiIRVector)";
							- _id = GUID c02073f7-4823-43dc-ad21-8f6ed6177fd8;
						}
					}
				}
				{ CGIClass 
					- _id = GUID f6673fd7-e0d3-469d-be7f-29ccaad52422;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 87;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "adc.sbs";
						- _subsystem = "Sources::hal::adc";
						- _class = "";
						- _name = "adc";
						- _id = GUID 5a90ee33-f857-4ba1-8f21-8cb807897c3a;
					}
					- m_pParent = GUID 30b86204-7654-490a-aee3-e3c056b75669;
					- m_name = { CGIText 
						- m_str = "hal::adc::adc";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2088;
					- m_transform = 0.373938 0 0 0.128342 239.252 1701.77 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_bFramesetModified = 1;
					- m_polygon = 4 2 329  2 1451  1061 1451  1061 329  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=17%,83%>
<frame name=AttributeListCompartment>
<frame name=PrimitiveOperationListCompartment>";
					- Attrs = { IRPYRawContainer 
						- size = 0;
					}
					- Operations = { IRPYRawContainer 
						- size = 4;
						- value = 
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "adc.sbs";
							- _subsystem = "Sources::hal::adc";
							- _class = "adc";
							- _name = "initAdc(adc_instance_t)";
							- _id = GUID 98365782-fe23-4cb9-a429-a66be2914a4a;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "adc.sbs";
							- _subsystem = "Sources::hal::adc";
							- _class = "adc";
							- _name = "startConversion(adc_instance_t)";
							- _id = GUID 4a3e1269-654d-4cac-be86-dda1155f66c8;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "adc.sbs";
							- _subsystem = "Sources::hal::adc";
							- _class = "adc";
							- _name = "isAdcDone(adc_instance_t)";
							- _id = GUID 6520112a-a0d7-46f3-89a9-96160101d57f;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "adc.sbs";
							- _subsystem = "Sources::hal::adc";
							- _class = "adc";
							- _name = "getValue(adc_instance_t)";
							- _id = GUID 4e66634b-f03b-4dfb-a092-6b2b3fc4e05e;
						}
					}
				}
				{ CGIClass 
					- _id = GUID 28074576-ddf8-47aa-85de-7fd656d2166a;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 87;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "diagnostics.sbs";
						- _subsystem = "Sources::hal::diagnostics";
						- _class = "";
						- _name = "diagnostics";
						- _id = GUID 072cf781-c2cc-4c85-9114-2ec4d3771de5;
					}
					- m_pParent = GUID 30b86204-7654-490a-aee3-e3c056b75669;
					- m_name = { CGIText 
						- m_str = "hal::diagnostics::diagnostics";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2088;
					- m_transform = 0.294618 0 0 0.159537 239.411 1861.51 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_bFramesetModified = 1;
					- m_polygon = 4 2 329  2 1451  1061 1451  1061 329  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=22%,78%>
<frame name=AttributeListCompartment>
<frame name=PrimitiveOperationListCompartment>";
					- Attrs = { IRPYRawContainer 
						- size = 0;
					}
					- Operations = { IRPYRawContainer 
						- size = 5;
						- value = 
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "diagnostics.sbs";
							- _subsystem = "Sources::hal::diagnostics";
							- _class = "diagnostics";
							- _name = "runDiagnostics()";
							- _id = GUID 40b1e726-10e7-4513-9106-e9cf53a27297;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "diagnostics.sbs";
							- _subsystem = "Sources::hal::diagnostics";
							- _class = "diagnostics";
							- _name = "btestIrArray()";
							- _id = GUID 1ec7aef0-1739-41d2-b2de-429093805fa5;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "diagnostics.sbs";
							- _subsystem = "Sources::hal::diagnostics";
							- _class = "diagnostics";
							- _name = "btestMotors()";
							- _id = GUID a60da37a-dd6e-43ce-8e1e-b5d773140566;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "diagnostics.sbs";
							- _subsystem = "Sources::hal::diagnostics";
							- _class = "diagnostics";
							- _name = "btestEncoders()";
							- _id = GUID 882aff1a-e368-4ce7-9619-dd70121b8491;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "diagnostics.sbs";
							- _subsystem = "Sources::hal::diagnostics";
							- _class = "diagnostics";
							- _name = "btestVSense()";
							- _id = GUID 96d779c6-ebb9-4587-ba9e-46412a3877d5;
						}
					}
				}
				{ CGIInheritance 
					- _id = GUID ff763f58-a0c2-4569-91da-47d74c92840c;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "target_definitions.sbs";
						- _subsystem = "Sources::hal::target_definitions";
						- _class = "target_pins";
						- _name = "MKL25Z4";
						- _id = GUID f5771fa4-b7f4-4d6d-abb8-c623d0a5291f;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "MKL25Z4";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID da185fd8-2eb7-44de-ab23-fc7519e2e0bb;
					- m_sourceType = 'F';
					- m_pTarget = GUID a0236fbe-b1d3-4b1f-9a96-3f7987100c8d;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 195 329 ;
					- m_TargetPort = 531 1392 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID 47ac81cd-8343-4fde-aff3-8c6e67569efb;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "main.sbs";
						- _subsystem = "Sources::main";
						- _class = "ES770";
						- _name = "target_pins";
						- _id = GUID ebf410a7-5a9f-4c46-a62a-548c02c91f05;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "target_pins";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID b5f6a8dc-1dcf-476a-9445-9ca434ee7a7f;
					- m_sourceType = 'F';
					- m_pTarget = GUID da185fd8-2eb7-44de-ab23-fc7519e2e0bb;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 2 1210 637  1210 952  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 1058 1337 ;
					- m_TargetPort = 2 347 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID 1a06df2e-87a8-4a73-a927-99ee5fcfb4b7;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "encoder.sbs";
						- _subsystem = "Sources::hal::encoder";
						- _class = "encoder";
						- _name = "target_pins";
						- _id = GUID 277cfce2-127a-4bb8-9b01-37d89e886893;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "target_pins";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 14cc5e3d-9af8-4d47-94a5-581348d066e0;
					- m_sourceType = 'F';
					- m_pTarget = GUID da185fd8-2eb7-44de-ab23-fc7519e2e0bb;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "Usage";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  62 -9  62 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 1302 825 ;
						- m_nHorizontalSpacing = 44;
						- m_nVerticalSpacing = -6;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 1056 1284 ;
					- m_TargetPort = 10 623 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID 552fc4c0-45ae-4370-9a7f-da633a7c03ea;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "driver.sbs";
						- _subsystem = "Sources::hal::driver";
						- _class = "driver";
						- _name = "target_pins";
						- _id = GUID a9ec3edf-5113-464d-ba56-1d23d418f262;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "target_pins";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 0634619c-fa98-4356-b802-05bb417607b5;
					- m_sourceType = 'F';
					- m_pTarget = GUID da185fd8-2eb7-44de-ab23-fc7519e2e0bb;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "Usage";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  62 -9  62 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 1266 1017 ;
						- m_nHorizontalSpacing = 43;
						- m_nVerticalSpacing = -5;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 2 1393 1462  1393 1492  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 1033 1271 ;
					- m_TargetPort = 2 765 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID 159c2784-1f05-44a8-9188-51041747c2dc;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "hmi.sbs";
						- _subsystem = "Sources::hal::hmi";
						- _class = "hmi";
						- _name = "target_pins";
						- _id = GUID 25af0f1b-cb43-41da-a197-eebc31fb2300;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "target_pins";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 2b78bb12-b9a1-4b17-9fd2-0381d921e35a;
					- m_sourceType = 'F';
					- m_pTarget = GUID da185fd8-2eb7-44de-ab23-fc7519e2e0bb;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "Usage";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  62 -9  62 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 1038 597 ;
						- m_nHorizontalSpacing = -65;
						- m_nVerticalSpacing = -6;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 2 1223 788  1223 1072  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 1061 744 ;
					- m_TargetPort = 2 454 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID 4957b79c-bdc7-4c64-94d9-87ccfda40935;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "adc.sbs";
						- _subsystem = "Sources::hal::adc";
						- _class = "adc";
						- _name = "target_pins";
						- _id = GUID a30701eb-5f0b-4a78-ba3e-a6cab8b5f716;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "target_pins";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID f6673fd7-e0d3-469d-be7f-29ccaad52422;
					- m_sourceType = 'F';
					- m_pTarget = GUID da185fd8-2eb7-44de-ab23-fc7519e2e0bb;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "Usage";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 1026 1381 ;
					- m_TargetPort = 2 1053 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID e10339a2-e2da-4dc3-b0a2-7a12c37cb76f;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "diagnostics.sbs";
						- _subsystem = "Sources::hal::diagnostics";
						- _class = "diagnostics";
						- _name = "target_pins";
						- _id = GUID 0c48226c-edad-4276-8f04-f8a23c2b2f0a;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "target_pins";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 28074576-ddf8-47aa-85de-7fd656d2166a;
					- m_sourceType = 'F';
					- m_pTarget = GUID da185fd8-2eb7-44de-ab23-fc7519e2e0bb;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "Usage";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  62 -9  62 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 1194 1497 ;
						- m_nHorizontalSpacing = 84;
						- m_nVerticalSpacing = -5;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 1020 693 ;
					- m_TargetPort = 2 1121 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID 7591abd9-c45e-46ad-a126-cea5a18a4aac;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "mcg.sbs";
						- _subsystem = "Sources::hal::mcg";
						- _class = "mcg";
						- _name = "fsl_clock_manager";
						- _id = GUID c8b43678-4b00-4671-a745-bbed721b7996;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "fsl_clock_manager";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8192;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 3f1f93f1-6e49-46b1-9c09-b94e874b0752;
					- m_sourceType = 'F';
					- m_pTarget = GUID dd0eb614-2c3f-424d-a65a-4b8096cb6e08;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "Usage";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  62 -9  62 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 498 333 ;
						- m_nHorizontalSpacing = -7;
						- m_nVerticalSpacing = -6;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 1 583 516  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 1060 1451 ;
					- m_TargetPort = 171 1395 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID bac44e4a-c03f-4d2e-9774-d8b6129716dd;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "hmi.sbs";
						- _subsystem = "Sources::hal::hmi";
						- _class = "hmi";
						- _name = "fsl_clock_manager";
						- _id = GUID c2ea0e4c-6fe5-42b1-afb2-de3f4e17e071;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "fsl_clock_manager";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8192;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 2b78bb12-b9a1-4b17-9fd2-0381d921e35a;
					- m_sourceType = 'F';
					- m_pTarget = GUID dd0eb614-2c3f-424d-a65a-4b8096cb6e08;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "Usage";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  62 -9  62 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 522 537 ;
						- m_nHorizontalSpacing = -23;
						- m_nVerticalSpacing = 37;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 977 863 ;
					- m_TargetPort = 540 1395 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID eb232221-48fa-42bc-b3cd-813b05e8de0b;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "encoder.sbs";
						- _subsystem = "Sources::hal::encoder";
						- _class = "encoder";
						- _name = "fsl_port_hal";
						- _id = GUID 548883b8-08ce-48d4-ba3a-d64ae1cb56f7;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "fsl_port_hal";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8192;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 14cc5e3d-9af8-4d47-94a5-581348d066e0;
					- m_sourceType = 'F';
					- m_pTarget = GUID 385df45c-8033-460a-b462-ac66640798cd;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "Usage";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  62 -9  62 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 762 489 ;
						- m_nHorizontalSpacing = 48;
						- m_nVerticalSpacing = 10;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 2 786 737  777 737  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 992 329 ;
					- m_TargetPort = 600 1382 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID 221362d0-fb2e-4de5-8862-d8325cfcfced;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "hmi.sbs";
						- _subsystem = "Sources::hal::hmi";
						- _class = "hmi";
						- _name = "controller";
						- _id = GUID e51581b1-230a-4a51-9f70-1168795fcec6;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "controller";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8192;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 2b78bb12-b9a1-4b17-9fd2-0381d921e35a;
					- m_sourceType = 'F';
					- m_pTarget = GUID 8809397d-2024-4fcf-bf49-a9c2cd53a733;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "Usage";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  62 -9  62 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 942 861 ;
						- m_nHorizontalSpacing = 49;
						- m_nVerticalSpacing = 199;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 1 906 910  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 1061 1347 ;
					- m_TargetPort = 1025 722 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID a054a09f-bd01-4761-9c3d-74573f92f8a1;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "encoder.sbs";
						- _subsystem = "Sources::hal::encoder";
						- _class = "encoder";
						- _name = "fsl_gpio_hal";
						- _id = GUID b7f5a7b4-ada3-417c-a67c-75ae3a214052;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "fsl_gpio_hal";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8192;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 14cc5e3d-9af8-4d47-94a5-581348d066e0;
					- m_sourceType = 'F';
					- m_pTarget = GUID df11025c-efd4-4b69-ad4e-10beeddee420;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "Usage";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  62 -9  62 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 1062 717 ;
						- m_nHorizontalSpacing = -36;
						- m_nVerticalSpacing = -58;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 1 1161 1195  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 1056 1274 ;
					- m_TargetPort = 483 1389 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID 7bc5f067-1aa7-4db4-8c59-ee10d50afff2;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "encoder.sbs";
						- _subsystem = "Sources::hal::encoder";
						- _class = "encoder";
						- _name = "fsl_interrupt_manager";
						- _id = GUID 8bcd0a89-99a3-43de-8997-6d61286513b0;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "fsl_interrupt_manager";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8192;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 14cc5e3d-9af8-4d47-94a5-581348d066e0;
					- m_sourceType = 'F';
					- m_pTarget = GUID cd04511f-e42f-4bc5-976b-9365a957c539;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "Usage";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  62 -9  62 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 1218 717 ;
						- m_nHorizontalSpacing = 1;
						- m_nVerticalSpacing = -114;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 1 1304 1196  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 1056 1279 ;
					- m_TargetPort = 492 1394 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID e638c293-f628-4dfa-8eac-1c4bca61290f;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "encoder.sbs";
						- _subsystem = "Sources::hal::encoder";
						- _class = "encoder";
						- _name = "fsl_tpm_driver";
						- _id = GUID fc1aa451-9e20-48d6-84ad-ac85ed59371c;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "fsl_tpm_driver";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 14cc5e3d-9af8-4d47-94a5-581348d066e0;
					- m_sourceType = 'F';
					- m_pTarget = GUID cd5f344e-b37b-4bb6-8075-1749de645be2;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "Usage";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  62 -9  62 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 1326 717 ;
						- m_nHorizontalSpacing = 34;
						- m_nVerticalSpacing = -114;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 1 1412 1195  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 1056 1274 ;
					- m_TargetPort = 110 1399 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID 8e9f34f0-2975-4af9-9cf8-7426b6b9fd1a;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "encoder.sbs";
						- _subsystem = "Sources::hal::encoder";
						- _class = "encoder";
						- _name = "fsl_tpm_hal";
						- _id = GUID 78ea596a-8ddc-4463-8ccf-9cfadd42aa45;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "fsl_tpm_hal";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 14cc5e3d-9af8-4d47-94a5-581348d066e0;
					- m_sourceType = 'F';
					- m_pTarget = GUID 83d40b69-423c-40e1-aa17-211583afebfb;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "Usage";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  62 -9  62 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 1446 717 ;
						- m_nHorizontalSpacing = 166;
						- m_nVerticalSpacing = -114;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 2 1130 1195  1130 496  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 1056 1274 ;
					- m_TargetPort = 98 1244 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID f187fd47-a263-4c52-8c73-ad2810ffa5ba;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "driver.sbs";
						- _subsystem = "Sources::hal::driver";
						- _class = "driver";
						- _name = "fsl_gpio_hal";
						- _id = GUID 9b1ae716-3157-49e7-a05b-a1690856f5ca;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "fsl_gpio_hal";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8192;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 0634619c-fa98-4356-b802-05bb417607b5;
					- m_sourceType = 'F';
					- m_pTarget = GUID df11025c-efd4-4b69-ad4e-10beeddee420;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "Usage";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  62 -9  62 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 1182 945 ;
						- m_nHorizontalSpacing = 49;
						- m_nVerticalSpacing = 8;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 1 1174 1463  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 1057 1278 ;
					- m_TargetPort = 610 1389 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID e3e0d5a5-bc8a-44dc-909a-6ebe1fb5c6f8;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "driver.sbs";
						- _subsystem = "Sources::hal::driver";
						- _class = "driver";
						- _name = "fsl_tpm_driver";
						- _id = GUID eb2ba8fc-5ee9-4968-94e3-4d3380f053ba;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "fsl_tpm_driver";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 0634619c-fa98-4356-b802-05bb417607b5;
					- m_sourceType = 'F';
					- m_pTarget = GUID cd5f344e-b37b-4bb6-8075-1749de645be2;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "Usage";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  62 -9  62 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 1338 945 ;
						- m_nHorizontalSpacing = -11;
						- m_nVerticalSpacing = -77;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 1 1424 1462  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 1057 1271 ;
					- m_TargetPort = 216 1185 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID 3435d1ed-c988-46a3-936e-10036baa79c8;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "driver.sbs";
						- _subsystem = "Sources::hal::driver";
						- _class = "driver";
						- _name = "fsl_tpm_hal";
						- _id = GUID 085b1fe0-a2c1-43d4-895a-43f4b08be777;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "fsl_tpm_hal";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 0634619c-fa98-4356-b802-05bb417607b5;
					- m_sourceType = 'F';
					- m_pTarget = GUID 83d40b69-423c-40e1-aa17-211583afebfb;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "Usage";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  62 -9  62 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 1446 945 ;
						- m_nHorizontalSpacing = 112;
						- m_nVerticalSpacing = -77;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 1 1460 1462  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 1057 1271 ;
					- m_TargetPort = 237 1387 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID d28fda40-6dd1-4af8-9e4e-add65d8d4ad1;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "driver.sbs";
						- _subsystem = "Sources::hal::driver";
						- _class = "driver";
						- _name = "fsl_pwm_driver";
						- _id = GUID bf19ff8c-3015-4310-a7c2-bbff88450b87;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "fsl_pwm_driver";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 0634619c-fa98-4356-b802-05bb417607b5;
					- m_sourceType = 'F';
					- m_pTarget = GUID c6fed933-846f-4b1e-bcee-5db64c97cf9f;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "Usage";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  62 -9  62 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 1470 897 ;
						- m_nHorizontalSpacing = 122;
						- m_nVerticalSpacing = -125;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 1 1556 1462  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 1057 1271 ;
					- m_TargetPort = 743 1388 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID 26ceb979-1535-42ab-8a6f-6d0e60d4a6ab;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "controller.sbs";
						- _subsystem = "Sources::hal::controller";
						- _class = "controller";
						- _name = "stdlib";
						- _id = GUID d341cacf-8104-44a3-b5b4-d24754dcdb34;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "stdlib";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 8809397d-2024-4fcf-bf49-a9c2cd53a733;
					- m_sourceType = 'F';
					- m_pTarget = GUID 1f185bb4-dde0-4611-9968-3b7ef2143784;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "Usage";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 1 1636 1672  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 1048 1152 ;
					- m_TargetPort = 322 1398 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIClass 
					- _id = GUID 734d9abe-aa95-4994-b216-91ac82610553;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Class";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "Font.Size";
												- _Value = "8";
												- _Type = Int;
											}
										}
									}
								}
							}
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 87;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "System.sbs";
						- _subsystem = "System";
						- _class = "";
						- _name = "fsl_adc16_driver";
						- _id = GUID af6b64a9-5b8a-483d-955a-d3d0008859ee;
					}
					- m_pParent = GUID 30b86204-7654-490a-aee3-e3c056b75669;
					- m_name = { CGIText 
						- m_str = "System::fsl_adc16_driver";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.0906516 0 0 0.0534759 1711.82 414.406 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_bFramesetModified = 1;
					- m_polygon = 4 2 329  2 1451  1061 1451  1061 329  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=39%,61%>
<frame name=AttributeListCompartment>
<frame name=PrimitiveOperationListCompartment>";
					- Attrs = { IRPYRawContainer 
						- size = 0;
					}
					- Operations = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIInheritance 
					- _id = GUID f19ef2e5-b703-4374-8639-248d5ed12c70;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "adc.sbs";
						- _subsystem = "Sources::hal::adc";
						- _class = "adc";
						- _name = "fsl_adc16_driver";
						- _id = GUID 42291047-d3cf-4b87-93aa-d69e17ce9e3f;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "fsl_adc16_driver";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID f6673fd7-e0d3-469d-be7f-29ccaad52422;
					- m_sourceType = 'F';
					- m_pTarget = GUID 734d9abe-aa95-4994-b216-91ac82610553;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "Usage";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  62 -9  62 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 1662 1341 ;
						- m_nHorizontalSpacing = 85;
						- m_nVerticalSpacing = -69;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 1 1752 1879  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 997 1381 ;
					- m_TargetPort = 399 1451 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID d1383428-9c1f-4c56-ae9c-185e7746c508;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "hmi.sbs";
						- _subsystem = "Sources::hal::hmi";
						- _class = "hmi";
						- _name = "fsl_debug_console";
						- _id = GUID 136e852a-269c-4dc0-851c-0a0088963325;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "fsl_debug_console";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8192;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 2b78bb12-b9a1-4b17-9fd2-0381d921e35a;
					- m_sourceType = 'F';
					- m_pTarget = GUID dd4802ab-723e-44db-882d-f8bb461ca68b;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "Usage";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  62 -9  62 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 1014 537 ;
						- m_nHorizontalSpacing = 177;
						- m_nVerticalSpacing = -66;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 1 1028 890  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 1061 1248 ;
					- m_TargetPort = 533 1188 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID 8ad77fdd-8d8e-45d6-b2fe-868c134826aa;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "mcg.sbs";
						- _subsystem = "Sources::hal::mcg";
						- _class = "mcg";
						- _name = "fsl_port_hal";
						- _id = GUID 6c10766e-8163-4fb5-a3fe-a70a9ec39294;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "fsl_port_hal";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8192;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 3f1f93f1-6e49-46b1-9c09-b94e874b0752;
					- m_sourceType = 'F';
					- m_pTarget = GUID 385df45c-8033-460a-b462-ac66640798cd;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "Usage";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  62 -9  62 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 666 333 ;
						- m_nHorizontalSpacing = 64;
						- m_nVerticalSpacing = -6;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 1 800 516  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 1060 1451 ;
					- m_TargetPort = 825 1400 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID d6dd873b-c543-4106-82ca-392f0f559d7c;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "mcg.sbs";
						- _subsystem = "Sources::hal::mcg";
						- _class = "mcg";
						- _name = "fsl_smc_hal";
						- _id = GUID 5be56881-40a6-4a81-a22a-547def2e3c7f;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "fsl_smc_hal";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8192;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 3f1f93f1-6e49-46b1-9c09-b94e874b0752;
					- m_sourceType = 'F';
					- m_pTarget = GUID 6515ce26-c133-4379-90a0-dd8d77d706f8;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "Usage";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  62 -9  62 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 882 321 ;
						- m_nHorizontalSpacing = 244;
						- m_nVerticalSpacing = -18;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 1 896 516  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 1014 1451 ;
					- m_TargetPort = 588 1393 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID 6acb9172-492d-46e5-9caf-608310d41a75;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "hmi.sbs";
						- _subsystem = "Sources::hal::hmi";
						- _class = "hmi";
						- _name = "fsl_port_hal";
						- _id = GUID 2ea18aea-1390-4d14-be6a-db25e9913343;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "fsl_port_hal";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8192;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 2b78bb12-b9a1-4b17-9fd2-0381d921e35a;
					- m_sourceType = 'F';
					- m_pTarget = GUID 385df45c-8033-460a-b462-ac66640798cd;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "Usage";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  62 -9  62 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 666 537 ;
						- m_nHorizontalSpacing = -20;
						- m_nVerticalSpacing = -40;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 1 749 892  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 1019 1258 ;
					- m_TargetPort = 326 1400 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID c114ac19-2573-4491-bb09-58a7f4ea995e;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "encoder.sbs";
						- _subsystem = "Sources::hal::encoder";
						- _class = "encoder";
						- _name = "fsl_clock_manager";
						- _id = GUID 9b9aa1c6-0a22-4e18-8ebb-3f7c639b8e7e;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "fsl_clock_manager";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8192;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 14cc5e3d-9af8-4d47-94a5-581348d066e0;
					- m_sourceType = 'F';
					- m_pTarget = GUID dd0eb614-2c3f-424d-a65a-4b8096cb6e08;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "Usage";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  62 -9  62 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 630 489 ;
						- m_nHorizontalSpacing = 50;
						- m_nVerticalSpacing = 10;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 2 651 737  680 737  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 746 329 ;
					- m_TargetPort = 886 1395 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID afb39004-46aa-438f-a6f2-b15bdb8d2b60;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "diagnostics.sbs";
						- _subsystem = "Sources::hal::diagnostics";
						- _class = "diagnostics";
						- _name = "fsl_gpio_hal";
						- _id = GUID 02065f42-5d63-4248-9ac9-25184edcc7fb;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "fsl_gpio_hal";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8192;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 28074576-ddf8-47aa-85de-7fd656d2166a;
					- m_sourceType = 'F';
					- m_pTarget = GUID df11025c-efd4-4b69-ad4e-10beeddee420;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "Usage";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  62 -9  62 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 1134 1281 ;
						- m_nHorizontalSpacing = 49;
						- m_nVerticalSpacing = -5;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 1 1149 2040  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 1020 1117 ;
					- m_TargetPort = 366 1175 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID 88f90356-1d6a-4298-9b35-f327bf002632;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "hmi.sbs";
						- _subsystem = "Sources::hal::hmi";
						- _class = "hmi";
						- _name = "fsl_smc_hal";
						- _id = GUID 0f5ac052-b0c4-4dfe-8b1f-533e970dbb59;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "fsl_smc_hal";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8192;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 2b78bb12-b9a1-4b17-9fd2-0381d921e35a;
					- m_sourceType = 'F';
					- m_pTarget = GUID 6515ce26-c133-4379-90a0-dd8d77d706f8;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "Usage";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  62 -9  62 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 858 537 ;
						- m_nHorizontalSpacing = 91;
						- m_nVerticalSpacing = -66;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 1 872 890  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 1061 1248 ;
					- m_TargetPort = 353 1393 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIClass 
					- _id = GUID cda74933-02b2-421f-a3f7-00ebb89201cb;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 87;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "util.sbs";
						- _subsystem = "Sources::hal::util";
						- _class = "";
						- _name = "tc_hal";
						- _id = GUID 57a158ce-caa1-4896-8f55-0c6ddcaca961;
					}
					- m_pParent = GUID 30b86204-7654-490a-aee3-e3c056b75669;
					- m_name = { CGIText 
						- m_str = "hal::util::tc_hal";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2088;
					- m_transform = 0.294618 0 0 0.0748663 240.411 2097.37 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_bFramesetModified = 1;
					- m_polygon = 4 2 329  2 1451  1061 1451  1061 329  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=20%,80%>
<frame name=AttributeListCompartment>
<frame name=PrimitiveOperationListCompartment>";
					- Attrs = { IRPYRawContainer 
						- size = 0;
					}
					- Operations = { IRPYRawContainer 
						- size = 1;
						- value = 
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "util.sbs";
							- _subsystem = "Sources::hal::util";
							- _class = "tc_hal";
							- _name = "installLptmr0(unsigned int,lptmr_callback_t)";
							- _id = GUID 6a338f0a-9b33-424b-a491-dba6759bccec;
						}
					}
				}
				{ CGIClass 
					- _id = GUID af64413e-9c2c-4966-8919-006fb07be7f2;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Class";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "Font.Size";
												- _Value = "8";
												- _Type = Int;
											}
										}
									}
								}
							}
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 87;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "System.sbs";
						- _subsystem = "System";
						- _class = "";
						- _name = "fsl_lptmr_driver";
						- _id = GUID 61c146f1-040d-458e-bf68-c6af2b177278;
					}
					- m_pParent = GUID 30b86204-7654-490a-aee3-e3c056b75669;
					- m_name = { CGIText 
						- m_str = "System::fsl_lptmr_driver";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.113314 0 0 0.0534759 1819.77 414.406 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 2 329  2 1451  1061 1451  1061 329  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=50%,50%>
<frame name=AttributeListCompartment>
<frame name=PrimitiveOperationListCompartment>";
					- Attrs = { IRPYRawContainer 
						- size = 0;
					}
					- Operations = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIInheritance 
					- _id = GUID 742834f7-4a34-4336-9932-ad4ba752f218;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "util.sbs";
						- _subsystem = "Sources::hal::util";
						- _class = "tc_hal";
						- _name = "fsl_lptmr_driver";
						- _id = GUID cfd9fff3-0fcf-415f-a20a-ce340387cfa7;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "fsl_lptmr_driver";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID cda74933-02b2-421f-a3f7-00ebb89201cb;
					- m_sourceType = 'F';
					- m_pTarget = GUID af64413e-9c2c-4966-8919-006fb07be7f2;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "Usage";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  62 -9  62 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 1770 1569 ;
						- m_nHorizontalSpacing = 93;
						- m_nVerticalSpacing = -42;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 1 1855 2182  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 1061 1130 ;
					- m_TargetPort = 311 1432 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIAnnotation 
					- _id = GUID 974e6d8c-7a75-445a-aeeb-31739bcb33ae;
					- m_type = 173;
					- m_pModelObject = { IHandle 
						- _m2Class = "IComment";
						- _filename = "Sources.sbs";
						- _subsystem = "Sources";
						- _class = "";
						- _name = "comment_45";
						- _id = GUID a420a8a7-dd6f-4d16-aa3f-11f741f5eee6;
					}
					- m_pParent = GUID 30b86204-7654-490a-aee3-e3c056b75669;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.409594 0 0 0.0989011 48 47.7033 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 0 3  0 1095  1084 1095  1084 3  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- _iTempdisplayTextFlag = 2;
					- m_bIsBoxStyle = 0;
				}
				{ CGIClass 
					- _id = GUID 479906cb-2de4-4258-ab42-82376361b89f;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 87;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "ir_array.sbs";
						- _subsystem = "Sources::hal::ir_array";
						- _class = "";
						- _name = "ir_array";
						- _id = GUID 380dee39-c5f8-4123-a799-f0061aacdb87;
					}
					- m_pParent = GUID 30b86204-7654-490a-aee3-e3c056b75669;
					- m_name = { CGIText 
						- m_str = "hal::ir_array::ir_array";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2088;
					- m_transform = 0.539188 0 0 0.221925 238.921 2178.98 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_bFramesetModified = 1;
					- m_polygon = 4 2 329  2 1451  1061 1451  1061 329  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=6%,94%>
<frame name=AttributeListCompartment>
<frame name=PrimitiveOperationListCompartment>";
					- Attrs = { IRPYRawContainer 
						- size = 0;
					}
					- Operations = { IRPYRawContainer 
						- size = 11;
						- value = 
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "ir_array.sbs";
							- _subsystem = "Sources::hal::ir_array";
							- _class = "ir_array";
							- _name = "initArray(array_instance_t)";
							- _id = GUID b056cded-3bb1-4125-aff4-5f45acee10c5;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "ir_array.sbs";
							- _subsystem = "Sources::hal::ir_array";
							- _class = "ir_array";
							- _name = "calibrate(array_instance_t)";
							- _id = GUID b89f89fc-0556-41ce-a5e3-db14aeb847e5;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "ir_array.sbs";
							- _subsystem = "Sources::hal::ir_array";
							- _class = "ir_array";
							- _name = "trackPos(array_instance_t)";
							- _id = GUID 94a11be2-2081-4430-8e51-1fe95fe7238e;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "ir_array.sbs";
							- _subsystem = "Sources::hal::ir_array";
							- _class = "ir_array";
							- _name = "ledSingleOn(uint8_t)";
							- _id = GUID 7ce5b5ab-377f-4e12-8d9a-9176bdb30584;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "ir_array.sbs";
							- _subsystem = "Sources::hal::ir_array";
							- _class = "ir_array";
							- _name = "ledArrayOn()";
							- _id = GUID cc3e56dc-7c1e-4037-b847-389def745a46;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "ir_array.sbs";
							- _subsystem = "Sources::hal::ir_array";
							- _class = "ir_array";
							- _name = "ledSingleOff(uint8_t)";
							- _id = GUID eb823cd0-a2e5-465a-a317-d7269e0609aa;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "ir_array.sbs";
							- _subsystem = "Sources::hal::ir_array";
							- _class = "ir_array";
							- _name = "takeSingleMeasurement(uint8_t)";
							- _id = GUID 0c02abef-d91a-46d0-93d9-b85bc05050f0;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "ir_array.sbs";
							- _subsystem = "Sources::hal::ir_array";
							- _class = "ir_array";
							- _name = "takeMeasurement()";
							- _id = GUID 939f54da-ee5a-44ec-aef4-82a45a4021bf;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "ir_array.sbs";
							- _subsystem = "Sources::hal::ir_array";
							- _class = "ir_array";
							- _name = "normalizeReadings(uint8_t,float)";
							- _id = GUID 11eb7676-be1c-44d5-b0ac-40e975c5dbe6;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "ir_array.sbs";
							- _subsystem = "Sources::hal::ir_array";
							- _class = "ir_array";
							- _name = "minMaxValuePosition(float,float,float,float,float,float,int)";
							- _id = GUID 8faae539-e346-47ed-9c23-19cc5d7c8f34;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "ir_array.sbs";
							- _subsystem = "Sources::hal::ir_array";
							- _class = "ir_array";
							- _name = "getPosition()";
							- _id = GUID 2a46afa5-2315-4dde-a5f7-e3076a44dcbd;
						}
					}
				}
				{ CGIInheritance 
					- _id = GUID 7f2cd4a4-ed9d-46fb-b91f-82584734cb27;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "ir_array.sbs";
						- _subsystem = "Sources::hal::ir_array";
						- _class = "ir_array";
						- _name = "target_pins";
						- _id = GUID c2715869-f047-41e2-ac38-a0a97164afe7;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "target_pins";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 479906cb-2de4-4258-ab42-82376361b89f;
					- m_sourceType = 'F';
					- m_pTarget = GUID da185fd8-2eb7-44de-ab23-fc7519e2e0bb;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "Usage";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 2 1359 2433  1359 2213  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 1024 1146 ;
					- m_TargetPort = 2 1300 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID 8c9b1295-d8a2-4e4d-97c9-992895006535;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "ir_array.sbs";
						- _subsystem = "Sources::hal::ir_array";
						- _class = "ir_array";
						- _name = "fsl_adc16_driver";
						- _id = GUID eab74722-5562-4e8f-851f-c5b0f2e7512c;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "fsl_adc16_driver";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 479906cb-2de4-4258-ab42-82376361b89f;
					- m_sourceType = 'F';
					- m_pTarget = GUID 734d9abe-aa95-4994-b216-91ac82610553;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "Usage";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  62 -9  62 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 1758 1677 ;
						- m_nHorizontalSpacing = 49;
						- m_nVerticalSpacing = -51;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 1 1773 2436  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 1024 1156 ;
					- m_TargetPort = 675 1414 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIAssociationEnd 
					- _id = GUID 1eac46be-ba5c-4e31-9e97-637664bd5f72;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 92;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAssociationEnd";
						- _filename = "main.sbs";
						- _subsystem = "Sources::main";
						- _class = "ES770";
						- _name = "itsHmi";
						- _id = GUID 91ce5788-66e3-4b7d-a8cd-63cf45d16311;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID b5f6a8dc-1dcf-476a-9445-9ca434ee7a7f;
					- m_sourceType = 'F';
					- m_pTarget = GUID 2b78bb12-b9a1-4b17-9fd2-0381d921e35a;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 7;
					}
					- m_arrow = 2 119 592  119 776  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 186 869 ;
					- m_TargetPort = 300 685 ;
					- m_pInverseModelObject = { IAssociationEndHandle 
						- _m2Class = "";
					}
					- m_pInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_pInverseInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_bShowSourceMultiplicity = 1;
					- m_bShowSourceRole = 0;
					- m_bShowTargetMultiplicity = 1;
					- m_bShowTargetRole = 0;
					- m_bShowLinkName = 1;
					- m_bShowSpecificType = 0;
					- m_bInstance = 0;
					- m_bShowQualifier1 = 1;
					- m_bShowQualifier2 = 1;
					- m_sourceRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 2;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_targetRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 3;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_sourceMultiplicity = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 4;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 4;
					}
					- m_targetMultiplicity = { CGIText 
						- m_str = "1";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 5;
						- m_bImplicitSetRectPoints = 0;
						- m_nHorizontalSpacing = -7;
						- m_nOrientationCtrlPt = 4;
					}
					- m_sourceQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 6;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_targetQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 7;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_specificType = type_122;
				}
				{ CGIAssociationEnd 
					- _id = GUID 275a985f-fd52-46dc-aa60-d38042bf306a;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 92;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAssociationEnd";
						- _filename = "main.sbs";
						- _subsystem = "Sources::main";
						- _class = "ES770";
						- _name = "itsEncoder";
						- _id = GUID 2d60c9a1-c0b4-451c-8eb1-5915d696f50c;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID b5f6a8dc-1dcf-476a-9445-9ca434ee7a7f;
					- m_sourceType = 'F';
					- m_pTarget = GUID 14cc5e3d-9af8-4d47-94a5-581348d066e0;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 7;
					}
					- m_arrow = 2 119 568  119 1204  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 48 620 ;
					- m_TargetPort = 134 1315 ;
					- m_pInverseModelObject = { IAssociationEndHandle 
						- _m2Class = "";
					}
					- m_pInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_pInverseInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_bShowSourceMultiplicity = 1;
					- m_bShowSourceRole = 0;
					- m_bShowTargetMultiplicity = 1;
					- m_bShowTargetRole = 0;
					- m_bShowLinkName = 1;
					- m_bShowSpecificType = 0;
					- m_bInstance = 0;
					- m_bShowQualifier1 = 1;
					- m_bShowQualifier2 = 1;
					- m_sourceRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 2;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_targetRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 3;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_sourceMultiplicity = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 4;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 4;
					}
					- m_targetMultiplicity = { CGIText 
						- m_str = "1";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 5;
						- m_bImplicitSetRectPoints = 0;
						- m_nHorizontalSpacing = -7;
						- m_nOrientationCtrlPt = 4;
					}
					- m_sourceQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 6;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_targetQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 7;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_specificType = type_122;
				}
				{ CGIAssociationEnd 
					- _id = GUID ea3c8e5f-2dbe-42b8-8c88-23a11cc7634c;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 92;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAssociationEnd";
						- _filename = "main.sbs";
						- _subsystem = "Sources::main";
						- _class = "ES770";
						- _name = "itsDriver";
						- _id = GUID a811307f-0ede-4425-ae4c-71732d08fe65;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID b5f6a8dc-1dcf-476a-9445-9ca434ee7a7f;
					- m_sourceType = 'F';
					- m_pTarget = GUID 0634619c-fa98-4356-b802-05bb417607b5;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 7;
					}
					- m_arrow = 2 120 568  120 1397  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 48 620 ;
					- m_TargetPort = 25 956 ;
					- m_pInverseModelObject = { IAssociationEndHandle 
						- _m2Class = "";
					}
					- m_pInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_pInverseInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_bShowSourceMultiplicity = 1;
					- m_bShowSourceRole = 0;
					- m_bShowTargetMultiplicity = 1;
					- m_bShowTargetRole = 0;
					- m_bShowLinkName = 1;
					- m_bShowSpecificType = 0;
					- m_bInstance = 0;
					- m_bShowQualifier1 = 1;
					- m_bShowQualifier2 = 1;
					- m_sourceRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 2;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_targetRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 3;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_sourceMultiplicity = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 4;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 4;
					}
					- m_targetMultiplicity = { CGIText 
						- m_str = "1";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 5;
						- m_bImplicitSetRectPoints = 0;
						- m_nHorizontalSpacing = -7;
						- m_nOrientationCtrlPt = 4;
					}
					- m_sourceQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 6;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_targetQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 7;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_specificType = type_122;
				}
				{ CGIAssociationEnd 
					- _id = GUID 8955f8ca-445c-4ac7-91c0-7625aa8b84cc;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 92;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAssociationEnd";
						- _filename = "main.sbs";
						- _subsystem = "Sources::main";
						- _class = "ES770";
						- _name = "itsController";
						- _id = GUID e3975edc-bcfc-47f1-b681-dd0053f4ea09;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID b5f6a8dc-1dcf-476a-9445-9ca434ee7a7f;
					- m_sourceType = 'F';
					- m_pTarget = GUID 8809397d-2024-4fcf-bf49-a9c2cd53a733;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 7;
					}
					- m_arrow = 2 120 567  120 1636  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 17 610 ;
					- m_TargetPort = 88 927 ;
					- m_pInverseModelObject = { IAssociationEndHandle 
						- _m2Class = "";
					}
					- m_pInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_pInverseInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_bShowSourceMultiplicity = 1;
					- m_bShowSourceRole = 0;
					- m_bShowTargetMultiplicity = 1;
					- m_bShowTargetRole = 0;
					- m_bShowLinkName = 1;
					- m_bShowSpecificType = 0;
					- m_bInstance = 0;
					- m_bShowQualifier1 = 1;
					- m_bShowQualifier2 = 1;
					- m_sourceRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 2;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_targetRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 3;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_sourceMultiplicity = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 4;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 4;
					}
					- m_targetMultiplicity = { CGIText 
						- m_str = "1";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 5;
						- m_bImplicitSetRectPoints = 0;
						- m_nHorizontalSpacing = -7;
						- m_nOrientationCtrlPt = 4;
					}
					- m_sourceQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 6;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_targetQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 7;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_specificType = type_122;
				}
				{ CGIAssociationEnd 
					- _id = GUID b4d55eab-8849-4c10-bc8d-f556ddd8116a;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 92;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAssociationEnd";
						- _filename = "main.sbs";
						- _subsystem = "Sources::main";
						- _class = "ES770";
						- _name = "itsAdc";
						- _id = GUID 616cc545-4986-4ae8-a4da-fb75fe75b90f;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID b5f6a8dc-1dcf-476a-9445-9ca434ee7a7f;
					- m_sourceType = 'F';
					- m_pTarget = GUID f6673fd7-e0d3-469d-be7f-29ccaad52422;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 7;
					}
					- m_arrow = 2 120 568  120 1864  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 2 620 ;
					- m_TargetPort = 34 1264 ;
					- m_pInverseModelObject = { IAssociationEndHandle 
						- _m2Class = "";
					}
					- m_pInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_pInverseInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_bShowSourceMultiplicity = 1;
					- m_bShowSourceRole = 0;
					- m_bShowTargetMultiplicity = 1;
					- m_bShowTargetRole = 0;
					- m_bShowLinkName = 1;
					- m_bShowSpecificType = 0;
					- m_bInstance = 0;
					- m_bShowQualifier1 = 1;
					- m_bShowQualifier2 = 1;
					- m_sourceRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 2;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_targetRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 3;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_sourceMultiplicity = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 4;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 4;
					}
					- m_targetMultiplicity = { CGIText 
						- m_str = "1";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 5;
						- m_bImplicitSetRectPoints = 0;
						- m_nHorizontalSpacing = -7;
						- m_nOrientationCtrlPt = 4;
					}
					- m_sourceQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 6;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_targetQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 7;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_specificType = type_122;
				}
				{ CGIAssociationEnd 
					- _id = GUID 7300e096-3876-4a65-a97b-fd18dd164bf4;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 92;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAssociationEnd";
						- _filename = "main.sbs";
						- _subsystem = "Sources::main";
						- _class = "ES770";
						- _name = "itsDiagnostics";
						- _id = GUID 86b4a032-7234-4118-84ec-2e49f0c7974b;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID b5f6a8dc-1dcf-476a-9445-9ca434ee7a7f;
					- m_sourceType = 'F';
					- m_pTarget = GUID 28074576-ddf8-47aa-85de-7fd656d2166a;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 7;
					}
					- m_arrow = 2 120 568  120 1960  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 48 620 ;
					- m_TargetPort = 165 617 ;
					- m_pInverseModelObject = { IAssociationEndHandle 
						- _m2Class = "";
					}
					- m_pInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_pInverseInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_bShowSourceMultiplicity = 1;
					- m_bShowSourceRole = 0;
					- m_bShowTargetMultiplicity = 1;
					- m_bShowTargetRole = 0;
					- m_bShowLinkName = 1;
					- m_bShowSpecificType = 0;
					- m_bInstance = 0;
					- m_bShowQualifier1 = 1;
					- m_bShowQualifier2 = 1;
					- m_sourceRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 2;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_targetRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 3;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_sourceMultiplicity = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 4;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 4;
					}
					- m_targetMultiplicity = { CGIText 
						- m_str = "1";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 5;
						- m_bImplicitSetRectPoints = 0;
						- m_nHorizontalSpacing = -7;
						- m_nOrientationCtrlPt = 4;
					}
					- m_sourceQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 6;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_targetQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 7;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_specificType = type_122;
				}
				{ CGIAssociationEnd 
					- _id = GUID 361e55ee-7686-48d2-aa5a-dc334edbe258;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 92;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAssociationEnd";
						- _filename = "main.sbs";
						- _subsystem = "Sources::main";
						- _class = "ES770";
						- _name = "itsTc_hal";
						- _id = GUID 105ccee0-05d9-410a-a40a-f2db5f40db28;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID b5f6a8dc-1dcf-476a-9445-9ca434ee7a7f;
					- m_sourceType = 'F';
					- m_pTarget = GUID cda74933-02b2-421f-a3f7-00ebb89201cb;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 7;
					}
					- m_arrow = 2 120 567  120 2131  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 90 610 ;
					- m_TargetPort = 206 449 ;
					- m_pInverseModelObject = { IAssociationEndHandle 
						- _m2Class = "";
					}
					- m_pInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_pInverseInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_bShowSourceMultiplicity = 1;
					- m_bShowSourceRole = 0;
					- m_bShowTargetMultiplicity = 1;
					- m_bShowTargetRole = 0;
					- m_bShowLinkName = 1;
					- m_bShowSpecificType = 0;
					- m_bInstance = 0;
					- m_bShowQualifier1 = 1;
					- m_bShowQualifier2 = 1;
					- m_sourceRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 2;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_targetRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 3;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_sourceMultiplicity = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 4;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 4;
					}
					- m_targetMultiplicity = { CGIText 
						- m_str = "1";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 5;
						- m_bImplicitSetRectPoints = 0;
						- m_nHorizontalSpacing = -7;
						- m_nOrientationCtrlPt = 4;
					}
					- m_sourceQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 6;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_targetQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 7;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_specificType = type_122;
				}
				{ CGIAssociationEnd 
					- _id = GUID f8f3a5bd-08f6-471c-bd66-c6b6ef642c5d;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 92;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAssociationEnd";
						- _filename = "main.sbs";
						- _subsystem = "Sources::main";
						- _class = "ES770";
						- _name = "itsIr_array";
						- _id = GUID 8ccdd3da-6fa4-49fa-aefc-74a63996c4ac;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID b5f6a8dc-1dcf-476a-9445-9ca434ee7a7f;
					- m_sourceType = 'F';
					- m_pTarget = GUID 479906cb-2de4-4258-ab42-82376361b89f;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 7;
					}
					- m_arrow = 2 120 568  120 2269  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 140 620 ;
					- m_TargetPort = 69 406 ;
					- m_pInverseModelObject = { IAssociationEndHandle 
						- _m2Class = "";
					}
					- m_pInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_pInverseInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_bShowSourceMultiplicity = 1;
					- m_bShowSourceRole = 0;
					- m_bShowTargetMultiplicity = 1;
					- m_bShowTargetRole = 0;
					- m_bShowLinkName = 1;
					- m_bShowSpecificType = 0;
					- m_bInstance = 0;
					- m_bShowQualifier1 = 1;
					- m_bShowQualifier2 = 1;
					- m_sourceRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 2;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_targetRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 3;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_sourceMultiplicity = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 4;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 4;
					}
					- m_targetMultiplicity = { CGIText 
						- m_str = "1";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 5;
						- m_bImplicitSetRectPoints = 0;
						- m_nHorizontalSpacing = -7;
						- m_nOrientationCtrlPt = 4;
					}
					- m_sourceQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 6;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_targetQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 7;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_specificType = type_122;
				}
				{ CGIAssociationEnd 
					- _id = GUID 02c53f3e-b5af-4df3-93eb-f8cad5a94ede;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 92;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAssociationEnd";
						- _filename = "main.sbs";
						- _subsystem = "Sources::main";
						- _class = "ES770";
						- _name = "itsMcg";
						- _id = GUID 3e26329a-6a4b-4b22-a246-621d84a654f2;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID b5f6a8dc-1dcf-476a-9445-9ca434ee7a7f;
					- m_sourceType = 'F';
					- m_pTarget = GUID 3f1f93f1-6e49-46b1-9c09-b94e874b0752;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 7;
					}
					- m_arrow = 2 119 591  119 458  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 17 859 ;
					- m_TargetPort = 164 909 ;
					- m_pInverseModelObject = { IAssociationEndHandle 
						- _m2Class = "";
					}
					- m_pInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_pInverseInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_bShowSourceMultiplicity = 1;
					- m_bShowSourceRole = 0;
					- m_bShowTargetMultiplicity = 1;
					- m_bShowTargetRole = 0;
					- m_bShowLinkName = 1;
					- m_bShowSpecificType = 0;
					- m_bInstance = 0;
					- m_bShowQualifier1 = 1;
					- m_bShowQualifier2 = 1;
					- m_sourceRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 2;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_targetRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 3;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_sourceMultiplicity = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 4;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 4;
					}
					- m_targetMultiplicity = { CGIText 
						- m_str = "1";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 5;
						- m_bImplicitSetRectPoints = 0;
						- m_nHorizontalSpacing = -7;
						- m_nOrientationCtrlPt = 4;
					}
					- m_sourceQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 6;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_targetQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 7;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_specificType = type_122;
				}
				{ CGIAssociationEnd 
					- _id = GUID 14fc801d-538a-4f97-a5c3-ff74a6149cb8;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 92;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAssociationEnd";
						- _filename = "main.sbs";
						- _subsystem = "Sources::main";
						- _class = "ES770";
						- _name = "itsTc_hal_1";
						- _id = GUID 28d2f332-1134-4ff4-aed1-b91cae32c6bb;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID b5f6a8dc-1dcf-476a-9445-9ca434ee7a7f;
					- m_sourceType = 'F';
					- m_pTarget = GUID ae6090bb-89f7-4802-8fbf-d9d3793b27f1;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 7;
					}
					- m_arrow = 2 120 591  120 373  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 21 859 ;
					- m_TargetPort = 100 689 ;
					- m_pInverseModelObject = { IAssociationEndHandle 
						- _m2Class = "";
					}
					- m_pInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_pInverseInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_bShowSourceMultiplicity = 1;
					- m_bShowSourceRole = 0;
					- m_bShowTargetMultiplicity = 1;
					- m_bShowTargetRole = 0;
					- m_bShowLinkName = 1;
					- m_bShowSpecificType = 0;
					- m_bInstance = 0;
					- m_bShowQualifier1 = 1;
					- m_bShowQualifier2 = 1;
					- m_sourceRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 2;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_targetRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 3;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_sourceMultiplicity = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 4;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 4;
					}
					- m_targetMultiplicity = { CGIText 
						- m_str = "1";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 5;
						- m_bImplicitSetRectPoints = 0;
						- m_nHorizontalSpacing = -7;
						- m_nOrientationCtrlPt = 4;
					}
					- m_sourceQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 6;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_targetQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 7;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_specificType = type_122;
				}
				{ CGIInheritance 
					- _id = GUID e72a8ee5-cc37-449b-9014-a38a4fec9c12;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "util.sbs";
						- _subsystem = "Sources::hal::util";
						- _class = "tc_hal";
						- _name = "mcg";
						- _id = GUID 8193131e-2755-469b-b28a-24be91066954;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "mcg";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID ae6090bb-89f7-4802-8fbf-d9d3793b27f1;
					- m_sourceType = 'F';
					- m_pTarget = GUID 3f1f93f1-6e49-46b1-9c09-b94e874b0752;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "Usage";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = -1 1293 ;
					- m_TargetPort = 1037 497 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIClass 
					- _id = GUID 538a5e25-591a-4c0a-b84b-e17a7a3f1fb3;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 87;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "vsense.sbs";
						- _subsystem = "Sources::hal::vsense";
						- _class = "";
						- _name = "vsense";
						- _id = GUID 1f0755b2-306c-4f25-b173-413abeb1548f;
					}
					- m_pParent = GUID 30b86204-7654-490a-aee3-e3c056b75669;
					- m_name = { CGIText 
						- m_str = "hal::vsense::vsense";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2088;
					- m_transform = 0.250236 0 0 0.190731 241.5 2488.25 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_bFramesetModified = 1;
					- m_polygon = 4 2 329  2 1451  1061 1451  1061 329  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=15%,85%>
<frame name=AttributeListCompartment>
<frame name=PrimitiveOperationListCompartment>";
					- Attrs = { IRPYRawContainer 
						- size = 0;
					}
					- Operations = { IRPYRawContainer 
						- size = 8;
						- value = 
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "vsense.sbs";
							- _subsystem = "Sources::hal::vsense";
							- _class = "vsense";
							- _name = "initVsense()";
							- _id = GUID 5e155c0a-90af-44df-b03e-731c9f306b66;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "vsense.sbs";
							- _subsystem = "Sources::hal::vsense";
							- _class = "vsense";
							- _name = "getRawV1()";
							- _id = GUID 9e841726-ce06-4402-90e7-ddf114cc5390;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "vsense.sbs";
							- _subsystem = "Sources::hal::vsense";
							- _class = "vsense";
							- _name = "getRawV2()";
							- _id = GUID c0345f85-0ee0-4081-ae6b-a16a9e6f8914;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "vsense.sbs";
							- _subsystem = "Sources::hal::vsense";
							- _class = "vsense";
							- _name = "getV1()";
							- _id = GUID b46fedc6-10f3-48b7-acd5-31c7f8997ff3;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "vsense.sbs";
							- _subsystem = "Sources::hal::vsense";
							- _class = "vsense";
							- _name = "getV2()";
							- _id = GUID 96784cb2-3799-4972-bdd6-fcdad6aab5bf;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "vsense.sbs";
							- _subsystem = "Sources::hal::vsense";
							- _class = "vsense";
							- _name = "getSystemVoltage()";
							- _id = GUID d2cbb5b8-ad26-4ef9-8682-8f6308dca410;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "vsense.sbs";
							- _subsystem = "Sources::hal::vsense";
							- _class = "vsense";
							- _name = "getCurrent()";
							- _id = GUID fec96cde-e1d0-4c79-bcba-da5feddeb451;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "vsense.sbs";
							- _subsystem = "Sources::hal::vsense";
							- _class = "vsense";
							- _name = "getPower()";
							- _id = GUID a55284c6-1ae6-4ba1-9156-c06ac7e0316b;
						}
					}
				}
				{ CGIAssociationEnd 
					- _id = GUID 5a009c46-355c-447c-92de-db8b26e4c3fb;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 92;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAssociationEnd";
						- _filename = "main.sbs";
						- _subsystem = "Sources::main";
						- _class = "ES770";
						- _name = "itsVsense";
						- _id = GUID d886eb5e-d9ef-4aba-87c5-28388817a2f4;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID b5f6a8dc-1dcf-476a-9445-9ca434ee7a7f;
					- m_sourceType = 'F';
					- m_pTarget = GUID 538a5e25-591a-4c0a-b84b-e17a7a3f1fb3;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 7;
					}
					- m_arrow = 2 120 592  120 2692  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 37 869 ;
					- m_TargetPort = 74 1068 ;
					- m_pInverseModelObject = { IAssociationEndHandle 
						- _m2Class = "IAssociationEnd";
						- _filename = "vsense.sbs";
						- _subsystem = "Sources::hal::vsense";
						- _class = "vsense";
						- _name = "itsES770";
						- _id = GUID a5b057cb-a11b-4841-9997-19d8b5772598;
					}
					- m_pInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_pInverseInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_bShowSourceMultiplicity = 1;
					- m_bShowSourceRole = 0;
					- m_bShowTargetMultiplicity = 1;
					- m_bShowTargetRole = 0;
					- m_bShowLinkName = 1;
					- m_bShowSpecificType = 0;
					- m_bInstance = 0;
					- m_bShowQualifier1 = 1;
					- m_bShowQualifier2 = 1;
					- m_sourceRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 2;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_targetRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 3;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_sourceMultiplicity = { CGIText 
						- m_str = "1";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 4;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 4;
					}
					- m_targetMultiplicity = { CGIText 
						- m_str = "1";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 5;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 4;
					}
					- m_sourceQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 6;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_targetQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 7;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_specificType = symmetric_type;
				}
				{ CGIInheritance 
					- _id = GUID 614624a8-1846-4a68-bf25-e76c5be2de02;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "True";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "vsense.sbs";
						- _subsystem = "Sources::hal::vsense";
						- _class = "vsense";
						- _name = "target_pins";
						- _id = GUID e3a49fe3-0047-479e-810a-0e7583812144;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "target_pins";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 538a5e25-591a-4c0a-b84b-e17a7a3f1fb3;
					- m_sourceType = 'F';
					- m_pTarget = GUID da185fd8-2eb7-44de-ab23-fc7519e2e0bb;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "Usage";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 2 1207 2682  1207 2062  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 933 1016 ;
					- m_TargetPort = 277 1188 ;
					- m_ShowName = 1;
					- m_ShowStereotype = 1;
				}
				
				- m_access = 'Z';
				- m_modified = 'N';
				- m_fileVersion = "";
				- m_nModifyDate = 0;
				- m_nCreateDate = 0;
				- m_creator = "";
				- m_bScaleWithZoom = 1;
				- m_arrowStyle = 'S';
				- m_pRoot = GUID 30b86204-7654-490a-aee3-e3c056b75669;
				- m_currentLeftTop = 0 0 ;
				- m_currentRightBottom = 0 0 ;
			}
			- _defaultSubsystem = { IHandle 
				- _m2Class = "ISubsystem";
				- _filename = "Sources.sbs";
				- _subsystem = "";
				- _class = "";
				- _name = "Sources";
				- _id = GUID f9623802-9e64-4088-b484-572be495c316;
			}
		}
	}
	- Components = { IRPYRawContainer 
		- size = 8;
		- value = 
		{ IComponent 
			- fileName = "FRDM_KL25Z";
			- _id = GUID e14c6d7e-2527-4591-8d47-f61912c80b65;
		}
		{ IComponent 
			- fileName = "Encoder_A";
			- _id = GUID ce24be95-baea-4ba5-9cd9-9124f23a155b;
		}
		{ IComponent 
			- fileName = "IR_Array";
			- _id = GUID 9d7eef10-fb9b-4f5d-ad99-d6368ca646c1;
		}
		{ IComponent 
			- fileName = "Encoder_B";
			- _id = GUID 199a0090-41bd-4581-ac47-f1c6366635f8;
		}
		{ IComponent 
			- fileName = "Motor_A";
			- _id = GUID 07dce727-5e4f-4cff-aa6c-39dfbb3e9658;
		}
		{ IComponent 
			- fileName = "Motor_B";
			- _id = GUID 5c9146fc-4bd2-422a-a71f-3f13a2125b14;
		}
		{ IComponent 
			- fileName = "Driver";
			- _id = GUID e8d2b136-7b20-43f7-91cd-12cd608855ae;
		}
		{ IComponent 
			- fileName = "Regulator_5V";
			- _id = GUID ab85102d-b980-4ba3-a86d-c3bffa018e58;
		}
	}
}

