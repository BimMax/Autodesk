import clr

clr.AddReference('System.Drawing')
clr.AddReference('System.Windows.Forms')
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *


class MainForm(Form):
    def __init__(self, view_templates, schedule_parameters, sheet_params,title_blocks_name,view_types):
        self.view_templates = view_templates
        self.schedule_parameters= schedule_parameters
        self.sheet_params = sheet_params
        self.title_blocks_name = title_blocks_name
        self.view_types = view_types
        self.InitializeComponent(self.view_templates,self.schedule_parameters, self.sheet_params, self.title_blocks_name,self.view_types)
        #self.vt = view_templates


    def InitializeComponent(self, view_templates, schedule_parameters, sheet_params,title_blocks_name,view_types):
        #resources = System.Resources.ResourceManager("foundationview.MainForm",
         #                                            System.Reflection.Assembly.GetEntryAssembly())
        self.vt = view_templates
        self.schedule_parameters=schedule_parameters
        self.title_blocks_name = title_blocks_name
        self.view_types = view_types

        self._pictureBox1 = System.Windows.Forms.PictureBox()
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self._label6 = System.Windows.Forms.Label()
        self._label7 = System.Windows.Forms.Label()
        self._label8 = System.Windows.Forms.Label()
        self._label9 = System.Windows.Forms.Label()
        self._Section1comboBox = System.Windows.Forms.ComboBox()
        self._groupBox1 = System.Windows.Forms.GroupBox()
        self._groupBox2 = System.Windows.Forms.GroupBox()
        self._PlanComboBox = System.Windows.Forms.ComboBox()
        self._checkBox2 = System.Windows.Forms.CheckBox()
        self._groupBox3 = System.Windows.Forms.GroupBox()
        self._checkBox3 = System.Windows.Forms.CheckBox()
        self._Section3comboBox = System.Windows.Forms.ComboBox()
        self._groupBox4 = System.Windows.Forms.GroupBox()
        self._checkBox4 = System.Windows.Forms.CheckBox()
        self._Section4comboBox = System.Windows.Forms.ComboBox()
        self._groupBox5 = System.Windows.Forms.GroupBox()
        self._groupBox6 = System.Windows.Forms.GroupBox()
        self._ScheduleParamenetrsComboBox1 = System.Windows.Forms.ComboBox()
        self._AcceptButton = System.Windows.Forms.Button()
        self._CancelButton = System.Windows.Forms.Button()
        self._groupBox7 = System.Windows.Forms.GroupBox()
        self._label10 = System.Windows.Forms.Label()
        self._SheetNumberTextBox = System.Windows.Forms.TextBox()
        self._SheetParameter1ComboBox = System.Windows.Forms.ComboBox()
        self._SheetParamaeter1Value = System.Windows.Forms.TextBox()
        self._SheetParamaeter2Value = System.Windows.Forms.TextBox()
        self._SheetParameter2ComboBox = System.Windows.Forms.ComboBox()
        self._label11 = System.Windows.Forms.Label()
        self._label12 = System.Windows.Forms.Label()
        self.__TextNoteBox = System.Windows.Forms.TextBox()
        self._label13 = System.Windows.Forms.Label()
        self._SectionViewFamilyTypeBox = System.Windows.Forms.ComboBox()
        self._label14 = System.Windows.Forms.Label()
        self._TitleblockComboBox = System.Windows.Forms.ComboBox()
        self._label15 = System.Windows.Forms.Label()
        self._label16 = System.Windows.Forms.Label()
        self._Section2comboBox = System.Windows.Forms.ComboBox()
        self._pictureBox1.BeginInit()
        self._groupBox1.SuspendLayout()
        self._groupBox2.SuspendLayout()
        self._groupBox3.SuspendLayout()
        self._groupBox4.SuspendLayout()
        self._groupBox5.SuspendLayout()
        self._groupBox6.SuspendLayout()
        self._groupBox7.SuspendLayout()
        self.SuspendLayout()
        #
        # pictureBox1
        #
        #self._pictureBox1.Image = resources.GetObject("pictureBox1.Image")
        self._pictureBox1.Location = System.Drawing.Point(-15, -4)
        self._pictureBox1.Name = "pictureBox1"
        self._pictureBox1.Size = System.Drawing.Size(570, 616)
        self._pictureBox1.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage
        self._pictureBox1.TabIndex = 0
        self._pictureBox1.TabStop = False
        self._pictureBox1.WaitOnLoad = True
        #self._pictureBox1.Click += self.PictureBox1Click
        #
        # label1
        #
        self._label1.BackColor = System.Drawing.SystemColors.ButtonHighlight
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Italic,
                                                System.Drawing.GraphicsUnit.Point, 204)
        self._label1.Location = System.Drawing.Point(283, 558)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(32, 23)
        self._label1.TabIndex = 1
        self._label1.Text = "1"
        #
        # label2
        #
        self._label2.BackColor = System.Drawing.SystemColors.ButtonHighlight
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Italic,
                                                System.Drawing.GraphicsUnit.Point, 204)
        self._label2.Location = System.Drawing.Point(293, 63)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(32, 23)
        self._label2.TabIndex = 1
        self._label2.Text = "1"
        #
        # label3
        #
        self._label3.BackColor = System.Drawing.SystemColors.ButtonHighlight
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Italic,
                                                System.Drawing.GraphicsUnit.Point, 204)
        self._label3.Location = System.Drawing.Point(55, 423)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(32, 23)
        self._label3.TabIndex = 1
        self._label3.Text = "3"
        #
        # label4
        #
        self._label4.BackColor = System.Drawing.SystemColors.ButtonHighlight
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Italic,
                                                System.Drawing.GraphicsUnit.Point, 204)
        self._label4.Location = System.Drawing.Point(448, 423)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(32, 23)
        self._label4.TabIndex = 1
        self._label4.Text = "3"
        #
        # label5
        #
        self._label5.BackColor = System.Drawing.SystemColors.ButtonHighlight
        self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Italic,
                                                System.Drawing.GraphicsUnit.Point, 204)
        self._label5.Location = System.Drawing.Point(55, 320)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(32, 23)
        self._label5.TabIndex = 1
        self._label5.Text = "4"
        self._label5.Click += self.Label5Click
        #
        # label6
        #
        self._label6.BackColor = System.Drawing.SystemColors.ButtonHighlight
        self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Italic,
                                                System.Drawing.GraphicsUnit.Point, 204)
        self._label6.Location = System.Drawing.Point(448, 320)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(32, 23)
        self._label6.TabIndex = 1
        self._label6.Text = "4"
        #
        # label7
        #
        self._label7.BackColor = System.Drawing.SystemColors.ButtonHighlight
        self._label7.Font = System.Drawing.Font("Microsoft Sans Serif", 10.2, System.Drawing.FontStyle.Regular,
                                                System.Drawing.GraphicsUnit.Point, 204)
        self._label7.Location = System.Drawing.Point(440, 114)
        self._label7.Name = "label7"
        self._label7.Size = System.Drawing.Size(98, 23)
        self._label7.TabIndex = 1
        self._label7.Text = "Plane"
        #
        # label8
        #
        self._label8.BackColor = System.Drawing.SystemColors.ButtonHighlight
        self._label8.Font = System.Drawing.Font("Microsoft Sans Serif", 10.2, System.Drawing.FontStyle.Regular,
                                                System.Drawing.GraphicsUnit.Point, 204)
        self._label8.Location = System.Drawing.Point(23, 114)
        self._label8.Name = "label8"
        self._label8.Size = System.Drawing.Size(61, 23)
        self._label8.TabIndex = 1
        self._label8.Text = "Plane"
        #
        # label9
        #
        self._label9.BackColor = System.Drawing.SystemColors.ButtonHighlight
        self._label9.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Italic,
                                                System.Drawing.GraphicsUnit.Point, 204)
        self._label9.Location = System.Drawing.Point(244, 9)
        self._label9.Name = "label9"
        self._label9.Size = System.Drawing.Size(59, 23)
        self._label9.TabIndex = 1
        self._label9.Text = "2-2"
        self._label9.Click += self.Label5Click
        #
        # Section1comboBox
        #
        self._Section1comboBox.FormattingEnabled = True
        self._Section1comboBox.Location = System.Drawing.Point(6, 24)
        self._Section1comboBox.Name = "Section1comboBox"
        self._Section1comboBox.Size = System.Drawing.Size(233, 24)
        self._Section1comboBox.TabIndex = 2
        #
        # groupBox1
        #
        self._groupBox1.BackColor = System.Drawing.SystemColors.ButtonHighlight
        self._groupBox1.Controls.Add(self._Section1comboBox)
        self._groupBox1.Location = System.Drawing.Point(293, 12)
        self._groupBox1.Name = "groupBox1"
        self._groupBox1.Size = System.Drawing.Size(259, 48)
        self._groupBox1.TabIndex = 3
        self._groupBox1.TabStop = False
        self._groupBox1.Text = "Template 1-1:"
        #
        # groupBox2
        #
        self._groupBox2.BackColor = System.Drawing.SystemColors.ButtonHighlight
        self._groupBox2.Controls.Add(self._checkBox2)
        self._groupBox2.Controls.Add(self._Section2comboBox)
        self._groupBox2.Location = System.Drawing.Point(-6, 12)
        self._groupBox2.Name = "groupBox2"
        self._groupBox2.Size = System.Drawing.Size(241, 89)
        self._groupBox2.TabIndex = 3
        self._groupBox2.TabStop = False
        self._groupBox2.Text = "Template 2-2:"
        #
        # PlanComboBox
        #
        self._PlanComboBox.FormattingEnabled = True
        self._PlanComboBox.Location = System.Drawing.Point(0, 177)
        self._PlanComboBox.Name = "PlanComboBox"
        self._PlanComboBox.Size = System.Drawing.Size(167, 24)
        self._PlanComboBox.TabIndex = 2
        #
        # checkBox2
        #
        self._checkBox2.Location = System.Drawing.Point(6, 54)
        self._checkBox2.Name = "checkBox2"
        self._checkBox2.Size = System.Drawing.Size(150, 24)
        self._checkBox2.TabIndex = 5
        self._checkBox2.Text = "via previous"
        self._checkBox2.UseVisualStyleBackColor = True
        self._checkBox2.CheckedChanged += self.CheckBox4CheckedChanged
        self._checkBox2.CheckState = System.Windows.Forms.CheckState.Checked
        #
        # groupBox3
        #
        self._groupBox3.BackColor = System.Drawing.SystemColors.ButtonHighlight
        self._groupBox3.Controls.Add(self._checkBox3)
        self._groupBox3.Controls.Add(self._Section3comboBox)
        self._groupBox3.Location = System.Drawing.Point(-6, 501)
        self._groupBox3.Name = "groupBox3"
        self._groupBox3.Size = System.Drawing.Size(241, 89)
        self._groupBox3.TabIndex = 3
        self._groupBox3.TabStop = False
        self._groupBox3.Text = "Template 3-3:"
        #
        # checkBox3
        #
        self._checkBox3.Location = System.Drawing.Point(6, 54)
        self._checkBox3.Name = "checkBox3"
        self._checkBox3.Size = System.Drawing.Size(150, 24)
        self._checkBox3.TabIndex = 5
        self._checkBox3.Text = "via previous"
        self._checkBox3.UseVisualStyleBackColor = True
        self._checkBox3.CheckedChanged += self.CheckBox4CheckedChanged
        self._checkBox3.CheckState = System.Windows.Forms.CheckState.Checked
        #
        # Section3comboBox
        #
        self._Section3comboBox.FormattingEnabled = True
        self._Section3comboBox.Location = System.Drawing.Point(6, 24)
        self._Section3comboBox.Name = "Section3comboBox"
        self._Section3comboBox.Size = System.Drawing.Size(233, 24)
        self._Section3comboBox.TabIndex = 2
        #
        # groupBox4
        #
        self._groupBox4.BackColor = System.Drawing.SystemColors.ButtonHighlight
        self._groupBox4.Controls.Add(self._checkBox4)
        self._groupBox4.Controls.Add(self._Section4comboBox)
        self._groupBox4.Location = System.Drawing.Point(316, 224)
        self._groupBox4.Name = "groupBox4"
        self._groupBox4.Size = System.Drawing.Size(241, 89)
        self._groupBox4.TabIndex = 3
        self._groupBox4.TabStop = False
        self._groupBox4.Text = "Template 4-4:"
        #
        # checkBox4
        #
        self._checkBox4.Location = System.Drawing.Point(6, 54)
        self._checkBox4.Name = "checkBox4"
        self._checkBox4.Size = System.Drawing.Size(150, 24)
        self._checkBox4.TabIndex = 5
        self._checkBox4.Text = "via previous"
        self._checkBox4.UseVisualStyleBackColor = True
        self._checkBox4.CheckedChanged += self.CheckBox4CheckedChanged
        self._checkBox4.CheckState = System.Windows.Forms.CheckState.Checked
        #
        # Section4comboBox
        #
        self._Section4comboBox.FormattingEnabled = True
        self._Section4comboBox.Location = System.Drawing.Point(6, 24)
        self._Section4comboBox.Name = "Section4comboBox"
        self._Section4comboBox.Size = System.Drawing.Size(233, 24)
        self._Section4comboBox.TabIndex = 2
        #
        # groupBox5
        #
        self._groupBox5.Controls.Add(self._CancelButton)
        self._groupBox5.Controls.Add(self._AcceptButton)
        self._groupBox5.Controls.Add(self._groupBox6)
        self._groupBox5.Location = System.Drawing.Point(558, 0)
        self._groupBox5.Name = "groupBox5"
        self._groupBox5.Size = System.Drawing.Size(380, 616)
        self._groupBox5.TabIndex = 4
        self._groupBox5.TabStop = False
        self._groupBox5.Text = "Parameters:"
        self._groupBox5.Enter += self.GroupBox5Enter
        #
        # groupBox6
        #
        self._groupBox6.Controls.Add(self._label15)
        self._groupBox6.Controls.Add(self._label14)
        self._groupBox6.Controls.Add(self._label13)
        self._groupBox6.Controls.Add(self._MainForm__TextNoteBox)
        self._groupBox6.Controls.Add(self._TitleblockComboBox)
        self._groupBox6.Controls.Add(self._groupBox7)
        self._groupBox6.Controls.Add(self._SectionViewFamilyTypeBox)
        self._groupBox6.Controls.Add(self._ScheduleParamenetrsComboBox1)
        self._groupBox6.Location = System.Drawing.Point(1, 36)
        self._groupBox6.Name = "groupBox6"
        self._groupBox6.Size = System.Drawing.Size(379, 543)
        self._groupBox6.TabIndex = 0
        self._groupBox6.TabStop = False
        self._groupBox6.Text = "Group schedule by parameter:"
        #
        # ScheduleParamenetrsComboBox1
        #
        self._ScheduleParamenetrsComboBox1.FormattingEnabled = True
        self._ScheduleParamenetrsComboBox1.Location = System.Drawing.Point(19, 26)
        self._ScheduleParamenetrsComboBox1.Name = "ScheduleParamenetrsComboBox1"
        self._ScheduleParamenetrsComboBox1.Size = System.Drawing.Size(346, 24)
        self._ScheduleParamenetrsComboBox1.TabIndex = 0

        #
        # AcceptButton
        #
        self._AcceptButton.Location = System.Drawing.Point(214, 588)
        self._AcceptButton.Name = "AcceptButton"
        self._AcceptButton.Size = System.Drawing.Size(75, 23)
        self._AcceptButton.TabIndex = 1
        self._AcceptButton.Text = "Ok"
        self._AcceptButton.UseVisualStyleBackColor = True
        self._AcceptButton.Click += self.AcceptButtonClick
        #
        # CancelButton
        #
        self._CancelButton.Location = System.Drawing.Point(295, 588)
        self._CancelButton.Name = "CancelButton"
        self._CancelButton.Size = System.Drawing.Size(75, 23)
        self._CancelButton.TabIndex = 1
        self._CancelButton.Text = "Cancel"
        self._CancelButton.UseVisualStyleBackColor = True
        self._CancelButton.Click += self.CancelButtonClick
        #
        # groupBox7
        #
        self._groupBox7.Controls.Add(self._SheetParameter2ComboBox)
        self._groupBox7.Controls.Add(self._SheetParamaeter2Value)
        self._groupBox7.Controls.Add(self._SheetParameter1ComboBox)
        self._groupBox7.Controls.Add(self._SheetParamaeter1Value)
        self._groupBox7.Controls.Add(self._SheetNumberTextBox)
        self._groupBox7.Controls.Add(self._label12)
        self._groupBox7.Controls.Add(self._label11)
        self._groupBox7.Controls.Add(self._label10)
        self._groupBox7.Location = System.Drawing.Point(12, 78)
        self._groupBox7.Name = "groupBox7"
        self._groupBox7.Size = System.Drawing.Size(357, 176)
        self._groupBox7.TabIndex = 1
        self._groupBox7.TabStop = False
        self._groupBox7.Text = "Sheet parameters:"
        #
        # label10
        #
        self._label10.Location = System.Drawing.Point(7, 31)
        self._label10.Name = "label10"
        self._label10.Size = System.Drawing.Size(177, 23)
        self._label10.TabIndex = 0
        self._label10.Text = "Sheet start number:"
        #
        # SheetNumberTextBox
        #
        self._SheetNumberTextBox.Location = System.Drawing.Point(251, 31)
        self._SheetNumberTextBox.Name = "SheetNumberTextBox"
        self._SheetNumberTextBox.Size = System.Drawing.Size(100, 22)
        self._SheetNumberTextBox.TabIndex = 1
        self._SheetNumberTextBox.TextChanged += self.SheetNumberTextBoxTextChanged
        #
        # SheetParameter1ComboBox
        #
        self._SheetParameter1ComboBox.FormattingEnabled = True
        self._SheetParameter1ComboBox.Location = System.Drawing.Point(7, 93)
        self._SheetParameter1ComboBox.Name = "SheetParameter1ComboBox"
        self._SheetParameter1ComboBox.Size = System.Drawing.Size(216, 24)
        self._SheetParameter1ComboBox.TabIndex = 2

        #
        # SheetParamaeter1Value
        #
        self._SheetParamaeter1Value.Location = System.Drawing.Point(251, 95)
        self._SheetParamaeter1Value.Name = "SheetParamaeter1Value"
        self._SheetParamaeter1Value.Size = System.Drawing.Size(100, 22)
        self._SheetParamaeter1Value.TabIndex = 1
        #
        # SheetParamaeter2Value
        #
        self._SheetParamaeter2Value.Location = System.Drawing.Point(251, 137)
        self._SheetParamaeter2Value.Name = "SheetParamaeter2Value"
        self._SheetParamaeter2Value.Size = System.Drawing.Size(100, 22)
        self._SheetParamaeter2Value.TabIndex = 1

        #
        # SheetParameter2ComboBox
        #
        self._SheetParameter2ComboBox.FormattingEnabled = True
        self._SheetParameter2ComboBox.Location = System.Drawing.Point(7, 135)
        self._SheetParameter2ComboBox.Name = "SheetParameter2ComboBox"
        self._SheetParameter2ComboBox.Size = System.Drawing.Size(216, 24)
        self._SheetParameter2ComboBox.TabIndex = 2

        #
        # label11
        #
        self._label11.Location = System.Drawing.Point(7, 68)
        self._label11.Name = "label11"
        self._label11.Size = System.Drawing.Size(216, 23)
        self._label11.TabIndex = 0
        self._label11.Text = "Parameter"
        self._label11.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        #
        # label12
        #
        self._label12.Location = System.Drawing.Point(251, 70)
        self._label12.Name = "label12"
        self._label12.Size = System.Drawing.Size(100, 23)
        self._label12.TabIndex = 0
        self._label12.Text = "Value"
        self._label12.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        #
        # TextNoteBox
        #
        self.__TextNoteBox.Location = System.Drawing.Point(19, 412)
        self.__TextNoteBox.Multiline = True
        self.__TextNoteBox.Name = "_TextNoteBox"
        self.__TextNoteBox.Size = System.Drawing.Size(344, 125)
        self.__TextNoteBox.TabIndex = 5
        #
        # label13
        #
        self._label13.Anchor = System.Windows.Forms.AnchorStyles.Left
        self._label13.Location = System.Drawing.Point(19, 385)
        self._label13.Name = "label13"
        self._label13.Size = System.Drawing.Size(100, 23)
        self._label13.TabIndex = 4
        self._label13.Text = "Text note:"
        self._label13.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        #
        # SectionViewFamilyTypeBox
        #
        self._SectionViewFamilyTypeBox.FormattingEnabled = True
        self._SectionViewFamilyTypeBox.Location = System.Drawing.Point(19, 279)
        self._SectionViewFamilyTypeBox.Name = "SectionViewFamilyTypeBox"
        self._SectionViewFamilyTypeBox.Size = System.Drawing.Size(346, 24)
        self._SectionViewFamilyTypeBox.TabIndex = 0
        #
        # label14
        #
        self._label14.Anchor = System.Windows.Forms.AnchorStyles.Left
        self._label14.Location = System.Drawing.Point(19, 253)
        self._label14.Name = "label14"
        self._label14.Size = System.Drawing.Size(154, 23)
        self._label14.TabIndex = 4
        self._label14.Text = "View family type:"
        self._label14.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        #
        # TitleblockComboBox
        #
        self._TitleblockComboBox.FormattingEnabled = True
        self._TitleblockComboBox.Location = System.Drawing.Point(19, 341)
        self._TitleblockComboBox.Name = "TitleblockComboBox"
        self._TitleblockComboBox.Size = System.Drawing.Size(346, 24)
        self._TitleblockComboBox.TabIndex = 0
        #
        # label15
        #
        self._label15.Anchor = System.Windows.Forms.AnchorStyles.Left
        self._label15.Location = System.Drawing.Point(19, 315)
        self._label15.Name = "label15"
        self._label15.Size = System.Drawing.Size(154, 23)
        self._label15.TabIndex = 4
        self._label15.Text = "Titleblock type:"
        self._label15.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        #
        # label16
        #
        self._label16.BackColor = System.Drawing.SystemColors.ButtonHighlight
        self._label16.Font = System.Drawing.Font("Microsoft Sans Serif", 10.2, System.Drawing.FontStyle.Regular,
                                                 System.Drawing.GraphicsUnit.Point, 204)
        self._label16.Location = System.Drawing.Point(0, 151)
        self._label16.Name = "label16"
        self._label16.Size = System.Drawing.Size(61, 23)
        self._label16.TabIndex = 1
        self._label16.Text = "Plane template"
        #
        # Section2comboBox
        #
        self._Section2comboBox.FormattingEnabled = True
        self._Section2comboBox.Location = System.Drawing.Point(6, 21)
        self._Section2comboBox.Name = "Section2comboBox"
        self._Section2comboBox.Size = System.Drawing.Size(235, 24)
        self._Section2comboBox.TabIndex = 2
        #
        # MainForm
        #
        self.ClientSize = System.Drawing.Size(944, 624)
        self.Controls.Add(self._groupBox5)
        self.Controls.Add(self._PlanComboBox)
        self.Controls.Add(self._groupBox4)
        self.Controls.Add(self._groupBox3)
        self.Controls.Add(self._groupBox2)
        self.Controls.Add(self._groupBox1)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label16)
        self.Controls.Add(self._label8)
        self.Controls.Add(self._label7)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._label9)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._pictureBox1)
        self.Name = "MainForm"
        self.Text = "foundationview"
        self._pictureBox1.EndInit()
        self._groupBox1.ResumeLayout(False)
        self._groupBox2.ResumeLayout(False)
        self._groupBox3.ResumeLayout(False)
        self._groupBox4.ResumeLayout(False)
        self._groupBox5.ResumeLayout(False)
        self._groupBox6.ResumeLayout(False)
        self._groupBox7.ResumeLayout(False)
        self._groupBox7.PerformLayout()
        self.ResumeLayout(False)

        #Add all values in combobox
        for template in self.vt:
            self._Section1comboBox.Items.Add(template)
            self._Section2comboBox.Items.Add(template)
            self._Section3comboBox.Items.Add(template)
            self._Section4comboBox.Items.Add(template)
            self._PlanComboBox.Items.Add(template)
        for parameter in self.schedule_parameters:
            self._ScheduleParamenetrsComboBox1.Items.Add(parameter)
        for parameter in self.sheet_params:
            self._SheetParameter1ComboBox.Items.Add(parameter)
            self._SheetParameter2ComboBox.Items.Add(parameter)

        for title in self.title_blocks_name:
            self._TitleblockComboBox.Items.Add(title)

        for type in self.view_types:
            self._SectionViewFamilyTypeBox.Items.Add(type)


    def Label5Click(self, sender, e):
        pass

    def SheetNumberTextBoxTextChanged(self, sender, e):
        pass

    def GroupBox5Enter(self, sender, e):
        pass

    def CancelButtonClick(self, sender, e):
        self.start = 0
        self.Close()

    def AcceptButtonClick(self, sender, e):

        self.temp_dict = {}
        self.temp_dict[0] = self._Section1comboBox.SelectedItem
        self.temp_dict[4] = self._PlanComboBox.SelectedItem
        self.comboboxes = [self._Section1comboBox,self._Section2comboBox, self._Section3comboBox, self._Section4comboBox, self._PlanComboBox]
        self.check_boxes = [self._checkBox2, self._checkBox3, self._checkBox4]
        i=1
        while i <4:
            if self.check_boxes[i-1].Checked:
                self.temp_dict[i]=self.comboboxes[i-1].SelectedItem
                self.comboboxes[i]=self.comboboxes[i-1]
            else:
                self.temp_dict[i]=self.comboboxes[i].SelectedItem
            i+=1
        self.schedule_group_parameter = self._ScheduleParamenetrsComboBox1.SelectedItem


        self.sheet_parameters_dict = {}
        self.sheet_parameters_dict[self._SheetParameter1ComboBox.SelectedItem] = self._SheetParamaeter1Value.Text
        self.sheet_parameters_dict[self._SheetParameter2ComboBox.SelectedItem] = self._SheetParamaeter2Value.Text
        self.SheetNumber = self._SheetNumberTextBox.Text
        self.title_block = self._TitleblockComboBox.SelectedItem
        self.view_type = self._SectionViewFamilyTypeBox.SelectedItem
        self.TextNote = self.__TextNoteBox.Text
        self.start =1
        self.Close()

    def TextNoteBoxSelectedIndexChanged(self, sender, e):
        pass

    def CheckBox3CheckedChanged(self, sender, e):
        pass

    def GroupBox8Enter(self, sender, e):
        pass

    def PlanComboBoxSelectedIndexChanged(self, sender, e):
        pass

    def CheckBox4CheckedChanged(self, sender, e):
        pass

    def CheckBox3CheckedChanged(self, sender, e):
        pass

    def CheckBox2CheckedChanged(self, sender, e):
        pass